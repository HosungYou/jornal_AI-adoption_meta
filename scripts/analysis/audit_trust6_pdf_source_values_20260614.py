#!/usr/bin/env python3
import csv, itertools, re, subprocess, tempfile
from pathlib import Path
from collections import defaultdict
REPO=Path(__file__).resolve().parents[2]
OUT=REPO/'data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614'
INPUT=OUT/'paper_a_latest_human_workbook_direct_r_input_20260614.csv'
SOURCE_PACKET_DIR=REPO/'data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets'
PDF_ROOTS=[Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/PDFs'), Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R1/PDFs'), Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R2/PDFs'), Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R3/PDFs'), Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R4/PDFs'), REPO/'data/02_screening/pdfs']
TRUST6=['PE','EE','SI','TRU','BI','UB']
REQ={'-'.join(sorted(p)) for p in itertools.combinations(TRUST6,2)}
def pair(a,b): return '-'.join(sorted([a,b]))
def value_variants(x):
    try: f=float(x)
    except: return []
    vals=set()
    for d in [2,3,4]:
        s=f'{f:.{d}f}'
        vals.add(s); vals.add(s.replace('0.','.')); vals.add(s.replace('-0.','-.'))
    vals.add(str(f))
    return sorted(vals, key=len, reverse=True)
def read_text_file(p):
    try: return p.read_text(errors='ignore')
    except: return ''
def pdf_text(p):
    try:
        r=subprocess.run(['pdftotext', str(p), '-'], text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=30)
        return r.stdout if r.returncode==0 else ''
    except Exception:
        return ''
def find_pdf(sid):
    hits=[]
    for root in PDF_ROOTS:
        p=root/f'{sid}.pdf'
        if p.exists(): hits.append(p)
    return hits
rows=list(csv.DictReader(INPUT.open()))
by_study=defaultdict(set)
for r in rows:
    if r['construct_1'] in TRUST6 and r['construct_2'] in TRUST6 and r['r_numeric'] and r['sample_size_numeric']:
        by_study[r['study_id']].add(pair(r['construct_1'],r['construct_2']))
complete=sorted([sid for sid,ps in by_study.items() if ps>=REQ])
records=[]
for sid in complete:
    packet=SOURCE_PACKET_DIR/f'{sid}_source_packet_20260609.txt'
    packet_text=read_text_file(packet)
    pdfs=find_pdf(sid)
    pdf_text_join='\n'.join(pdf_text(p) for p in pdfs[:1]) if pdfs else ''
    # all coded rows for required trust6 pairs
    relevant=[r for r in rows if r['study_id']==sid and pair(r['construct_1'],r['construct_2']) in REQ and r['r_numeric']]
    # collapse exact duplicate source rows for readability
    seen=set()
    for r in relevant:
        key=(sid,pair(r['construct_1'],r['construct_2']),r['r_numeric'],r['source_file'],r['source_location'])
        if key in seen: continue
        seen.add(key)
        variants=value_variants(r['r_numeric'])
        packet_hit=any(v and v in packet_text for v in variants)
        pdf_hit=any(v and v in pdf_text_join for v in variants)
        records.append({
            'study_id':sid,'pair':pair(r['construct_1'],r['construct_2']),'construct_1':r['construct_1'],'construct_2':r['construct_2'],'r_numeric':r['r_numeric'],'sample_size_numeric':r['sample_size_numeric'],'source_file':r['source_file'],'source_location':r.get('source_location',''),'source_packet_exists':packet.exists(),'pdf_exists':bool(pdfs),'pdf_path':str(pdfs[0]) if pdfs else '', 'value_found_in_source_packet_text':packet_hit,'value_found_in_pdf_text':pdf_hit,'flag':r.get('flag',''),'notes':r.get('notes','')
        })
fields=['study_id','pair','construct_1','construct_2','r_numeric','sample_size_numeric','source_file','source_location','source_packet_exists','pdf_exists','pdf_path','value_found_in_source_packet_text','value_found_in_pdf_text','flag','notes']
with (OUT/'trust6_complete_case_pdf_source_value_audit_20260614.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(records)
study_summary=[]
for sid in complete:
    rec=[r for r in records if r['study_id']==sid]
    study_summary.append({'study_id':sid,'coded_rows':len(rec),'unique_pairs':len(set(r['pair'] for r in rec)),'source_packet_exists':any(r['source_packet_exists'] for r in rec),'pdf_exists':any(r['pdf_exists'] for r in rec),'rows_value_found_in_source_packet_text':sum(str(r['value_found_in_source_packet_text'])=='True' for r in rec),'rows_value_found_in_pdf_text':sum(str(r['value_found_in_pdf_text'])=='True' for r in rec)})
with (OUT/'trust6_complete_case_pdf_source_value_audit_summary_20260614.csv').open('w',newline='',encoding='utf-8') as f:
    fields2=['study_id','coded_rows','unique_pairs','source_packet_exists','pdf_exists','rows_value_found_in_source_packet_text','rows_value_found_in_pdf_text']
    w=csv.DictWriter(f,fieldnames=fields2); w.writeheader(); w.writerows(study_summary)
report=['# Trust6 Complete-Case PDF/Source Value Audit','', 'Date: 2026-06-14','', 'Scope: automated source presence check for the 8 latest-human-workbook trust6 complete-case studies. This checks local PDF/source-packet availability and simple numeric value presence in extracted text; it is not a final manual table-level adjudication.', '', '| Study | Unique trust6 pairs | Source packet | PDF | Rows with value in source packet text | Rows with value in PDF text |', '| --- | ---: | --- | --- | ---: | ---: |']
for s in study_summary:
    report.append(f"| {s['study_id']} | {s['unique_pairs']} | {s['source_packet_exists']} | {s['pdf_exists']} | {s['rows_value_found_in_source_packet_text']}/{s['coded_rows']} | {s['rows_value_found_in_pdf_text']}/{s['coded_rows']} |")
report += ['', 'Interpretation: failures to find a value in raw `pdftotext` output are not definitive evidence that the coding is wrong, because tables may be split or rendered poorly. Positive hits support that the coded value is visible in local source text. Full source adjudication still requires human/PDF table inspection for flagged rows.']
(OUT/'TRUST6_COMPLETE_CASE_PDF_SOURCE_VALUE_AUDIT_20260614.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
print('\n'.join(report))
