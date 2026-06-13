#!/usr/bin/env python3
import csv, math, re, json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from collections import defaultdict, Counter

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614'
OUT.mkdir(parents=True, exist_ok=True)
TARGET = ['PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB']
TARGET_SET = set(TARGET)
WORKBOOKS = {
    'R1': Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_20260425.xlsx'),
    'R2': Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R2_Phase0_1_2_20260425.xlsx'),
    'R3': Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R3_Phase0_1_2_20260425.xlsx'),
    'R4': Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R4_Phase0_1_2_20260425_v2.xlsx'),
}
CURRENT_INPUT = REPO / 'data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv'
NS = {'a':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','rel':'http://schemas.openxmlformats.org/package/2006/relationships'}

def col_index(ref):
    letters = ''.join(ch for ch in ref if ch.isalpha())
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch.upper()) - 64
    return n

def shared_strings(z):
    if 'xl/sharedStrings.xml' not in z.namelist(): return []
    root = ET.fromstring(z.read('xl/sharedStrings.xml'))
    return [''.join(t.text or '' for t in si.findall('.//a:t', NS)) for si in root.findall('a:si', NS)]

def cell_value(c, ss):
    t = c.attrib.get('t')
    if t == 'inlineStr': return ''.join(x.text or '' for x in c.findall('.//a:t', NS)).strip()
    v = c.find('a:v', NS)
    if v is None: return ''
    val = (v.text or '').strip()
    if t == 's':
        try: return ss[int(val)].strip()
        except Exception: return val
    return val

def resolve_target(target):
    target = target.lstrip('/')
    if target.startswith('xl/'): return target
    return str(PurePosixPath('xl') / target)

def sheet_map(z):
    wb = ET.fromstring(z.read('xl/workbook.xml'))
    rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rid_to_target = {r.attrib['Id']: resolve_target(r.attrib['Target']) for r in rels.findall('rel:Relationship', NS)}
    out = {}
    for s in wb.findall('.//a:sheet', NS):
        rid = s.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        out[s.attrib['name']] = rid_to_target[rid]
    return out

def read_sheet(path, sheet_name):
    with ZipFile(path) as z:
        ss = shared_strings(z)
        smap = sheet_map(z)
        target = smap[sheet_name]
        root = ET.fromstring(z.read(target))
        parsed_rows = []
        for row in root.findall('.//a:sheetData/a:row', NS):
            vals = {}
            for c in row.findall('a:c', NS):
                vals[col_index(c.attrib.get('r','A1'))] = cell_value(c, ss)
            if vals:
                maxc = max(vals)
                parsed_rows.append([vals.get(i, '') for i in range(1, maxc + 1)])
        if not parsed_rows: return []
        header_i = None
        for i, row in enumerate(parsed_rows[:20]):
            low = [str(x).strip().lower() for x in row]
            if 'study_id' in low or 'x' in low:
                header_i = i; break
        if header_i is None: return []
        headers = [str(x).strip() for x in parsed_rows[header_i]]
        rows = []
        for row in parsed_rows[header_i+1:]:
            rec = {headers[i]: (row[i] if i < len(row) else '') for i in range(len(headers)) if headers[i]}
            if any(str(v).strip() for v in rec.values()): rows.append(rec)
        return rows

def canon_construct(x):
    x = str(x or '').strip().upper().replace(' ', '')
    aliases = {'TRUST':'TRU','SELF-EFFICACY':'SE','SELFEFFICACY':'SE','ANXIETY':'ANX','ATTITUDE':'ATT','USEBEHAVIOR':'UB','BEHAVIORALINTENTION':'BI'}
    return aliases.get(x, x)

def canon_pair(a,b):
    a,b = canon_construct(a), canon_construct(b)
    return '-'.join(sorted([a,b]))

def num(x):
    s = str(x or '').strip()
    if s == '': return None
    s = s.replace(',', '')
    m = re.search(r'-?\d+(?:\.\d+)?', s)
    if not m: return None
    try: return float(m.group(0))
    except Exception: return None

metadata = {}
meta_rows = []
corr_rows = []
for coder, path in WORKBOOKS.items():
    mrows = read_sheet(path, 'STUDY_METADATA')
    for r in mrows:
        sid = str(r.get('study_id') or r.get('x') or '').strip()
        if not sid: continue
        n = num(r.get('sample_size'))
        metadata[(coder, sid)] = r
        meta_rows.append({'coder': coder, 'study_id': sid, 'sample_size': n, 'title': r.get('title',''), 'first_author': r.get('first_author',''), 'year': r.get('year','')})
    sheets = ['CORRELATIONS']
    if coder == 'R3': sheets = ['(합의) CORRELATIONS', 'CORRELATIONS']
    for sh in sheets:
        try: rows = read_sheet(path, sh)
        except KeyError: rows = []
        for r in rows:
            sid = str(r.get('study_id') or '').strip()
            c1, c2 = canon_construct(r.get('construct_1')), canon_construct(r.get('construct_2'))
            rv = num(r.get('r_value'))
            beta = num(r.get('original_beta'))
            if not sid or not c1 or not c2: continue
            if c1 not in TARGET_SET or c2 not in TARGET_SET or c1 == c2: continue
            corr_rows.append({
                'coder': coder, 'sheet': sh, 'study_id': sid, 'construct_1': c1, 'construct_2': c2, 'pair': canon_pair(c1,c2),
                'r_value': rv, 'original_beta': beta, 'r_source': r.get('r_source',''), 'source_location': r.get('source_location',''), 'flag': r.get('flag',''), 'notes': r.get('notes',''),
                'sample_size': metadata.get((coder, sid), {}).get('sample_size')
            })

# Current input rows.
current_rows = []
with CURRENT_INPUT.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        c1, c2 = canon_construct(r.get('construct_1')), canon_construct(r.get('construct_2'))
        rv = num(r.get('r_numeric'))
        if c1 in TARGET_SET and c2 in TARGET_SET and c1 != c2 and rv is not None and abs(rv) < 1:
            current_rows.append({'study_id': str(r.get('study_id','')).strip(), 'construct_1': c1, 'construct_2': c2, 'pair': canon_pair(c1,c2), 'r_value': rv, 'sample_size': num(r.get('sample_size_numeric')), 'source_file': r.get('source_file',''), 'row_decision': r.get('row_decision','')})

def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

def summarize(rows, label):
    studies = sorted({r['study_id'] for r in rows})
    pairs = sorted({r['pair'] for r in rows})
    numeric = [r for r in rows if r.get('r_value') is not None]
    study_pair = {(r['study_id'], r['pair']) for r in numeric}
    per_study = defaultdict(set)
    for r in numeric: per_study[r['study_id']].add(r['pair'])
    required = math.comb(len(TARGET),2)
    complete = sum(1 for sid, ps in per_study.items() if len(ps) == required)
    ge15 = sum(1 for sid, ps in per_study.items() if len(ps) >= 15)
    return {'dataset': label, 'rows': len(rows), 'numeric_rows': len(numeric), 'studies': len(studies), 'pairs': len(pairs), 'required_pairs': required, 'missing_pairs': required-len(pairs), 'study_pair_cells': len(study_pair), 'complete_10construct_studies': complete, 'studies_with_15plus_pairs': ge15}

# De-duplicate latest human rows by coder/sheet/study/pair/r for summary, but keep raw detail.
latest_numeric = [r for r in corr_rows if r['r_value'] is not None and abs(r['r_value']) < 1]
current_key = {(r['study_id'], r['pair'], round(r['r_value'], 6)) for r in current_rows}
latest_key = {(r['study_id'], r['pair'], round(r['r_value'], 6)) for r in latest_numeric}
missing_from_current = [r for r in latest_numeric if (r['study_id'], r['pair'], round(r['r_value'], 6)) not in current_key]
current_not_in_latest = [r for r in current_rows if (r['study_id'], r['pair'], round(r['r_value'], 6)) not in latest_key]

# Study-pair level comparison ignoring exact value.
current_sp = {(r['study_id'], r['pair']) for r in current_rows}
latest_sp = {(r['study_id'], r['pair']) for r in latest_numeric}
missing_studypair = [r for r in latest_numeric if (r['study_id'], r['pair']) not in current_sp]
current_extra_studypair = [r for r in current_rows if (r['study_id'], r['pair']) not in latest_sp]

summary = [summarize(latest_numeric, 'latest_R1_R4_human_workbooks'), summarize(current_rows, 'current_20260612_rerun_input')]
write_csv(OUT / 'latest_human_workbook_correlations_20260614.csv', corr_rows, ['coder','sheet','study_id','construct_1','construct_2','pair','r_value','original_beta','r_source','source_location','flag','notes','sample_size'])
write_csv(OUT / 'latest_human_workbook_metadata_20260614.csv', meta_rows, ['coder','study_id','sample_size','title','first_author','year'])
write_csv(OUT / 'latest_vs_current_exact_value_missing_from_current_20260614.csv', missing_from_current, ['coder','sheet','study_id','construct_1','construct_2','pair','r_value','original_beta','r_source','source_location','flag','notes','sample_size'])
write_csv(OUT / 'latest_vs_current_studypair_missing_from_current_20260614.csv', missing_studypair, ['coder','sheet','study_id','construct_1','construct_2','pair','r_value','original_beta','r_source','source_location','flag','notes','sample_size'])
write_csv(OUT / 'current_studypair_not_in_latest_human_20260614.csv', current_extra_studypair, ['study_id','construct_1','construct_2','pair','r_value','sample_size','source_file','row_decision'])
write_csv(OUT / 'latest_human_vs_current_summary_20260614.csv', summary, ['dataset','rows','numeric_rows','studies','pairs','required_pairs','missing_pairs','study_pair_cells','complete_10construct_studies','studies_with_15plus_pairs'])

# Build a latest human direct-r input for rerun, with sample size from same coder metadata where possible.
rerun = []
seen = set()
for r in latest_numeric:
    key = (r['coder'], r['sheet'], r['study_id'], r['pair'], r['r_value'])
    if key in seen: continue
    seen.add(key)
    rerun.append({
        'study_id': r['study_id'], 'construct_1': r['construct_1'], 'construct_2': r['construct_2'], 'r_numeric': r['r_value'],
        'sample_size_numeric': r.get('sample_size') or '', 'source_file': f"latest_human_{r['coder']}_{r['sheet']}", 'source_location': r.get('source_location',''), 'flag': r.get('flag',''), 'notes': r.get('notes','')
    })
write_csv(OUT / 'paper_a_latest_human_workbook_direct_r_input_20260614.csv', rerun, ['study_id','construct_1','construct_2','r_numeric','sample_size_numeric','source_file','source_location','flag','notes'])

report = []
report += ['# Paper A Latest Human Workbook Audit', '', 'Date: 2026-06-14', '']
report += ['## Source workbooks', '']
for coder, path in WORKBOOKS.items(): report.append(f'- `{coder}`: `{path}`')
report += ['', '## Summary', '', '| Dataset | Numeric rows | Studies | Pairs | Missing pairs | Complete full10 studies | Studies with >=15 pairs |', '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
for s in summary: report.append(f"| {s['dataset']} | {s['numeric_rows']} | {s['studies']} | {s['pairs']}/{s['required_pairs']} | {s['missing_pairs']} | {s['complete_10construct_studies']} | {s['studies_with_15plus_pairs']} |")
report += ['', '## Comparison to current 20260612 rerun input', '']
report.append(f'- Latest human workbook study-pair cells not represented in current input: {len({(r["study_id"], r["pair"]) for r in missing_studypair})}')
report.append(f'- Current input study-pair cells not represented in latest raw human workbook rows: {len({(r["study_id"], r["pair"]) for r in current_extra_studypair})}')
report.append(f'- Exact study-pair-value rows from latest workbooks absent from current input: {len(missing_from_current)}')
report += ['', '## Interpretation', '']
report.append('The provided Drive folder is not sufficient as the final human-value source because Drive search and local OneDrive traces show later modified R1/R2/R3 files and an R4 v2 file. The latest local read-only copies under `Coding_Latest_R1_R4_20260605` should be treated as the first candidate final human-workbook set for this audit.')
report.append('This audit does not yet prove PDF/source correctness. It only establishes whether the current analytic input appears to omit or transform rows relative to the latest human workbook set.')
(OUT / 'PAPER_A_LATEST_HUMAN_WORKBOOK_AUDIT_20260614.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
print('\n'.join(report))
