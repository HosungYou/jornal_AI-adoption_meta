#!/usr/bin/env python3
"""
Deduplication and merging of search results from multiple databases.
Uses DOI exact matching and fuzzy title matching.
"""

import pandas as pd
from pathlib import Path
from typing import List, Dict, Any
import logging
from difflib import SequenceMatcher

logger = logging.getLogger(__name__)


class RecordDeduplicator:
    """Deduplicates and merges records from multiple database searches."""

    def __init__(self, title_similarity_threshold: float = 0.90):
        """
        Initialize deduplicator.

        Args:
            title_similarity_threshold: Minimum similarity for title matching (0-1)
        """
        self.title_similarity_threshold = title_similarity_threshold
        self.required_columns = ["title"]
        self.optional_columns = ["abstract", "keywords", "year", "doi"]

    def validate_schema(self, df: pd.DataFrame, db_name: str):
        """Validate minimum schema and normalize optional columns."""
        missing_required = [c for c in self.required_columns if c not in df.columns]
        if missing_required:
            raise ValueError(f"{db_name}: missing required columns: {missing_required}")

        for col in self.optional_columns:
            if col not in df.columns:
                df[col] = ""
                logger.warning("%s: optional column '%s' missing; filled with blank", db_name, col)

    def normalize_title(self, title: str) -> str:
        """
        Normalize title for comparison.

        Args:
            title: Raw title

        Returns:
            Normalized title
        """
        if pd.isna(title):
            return ""

        # Convert to lowercase
        normalized = str(title).lower()

        # Remove punctuation
        normalized = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in normalized)

        # Remove extra whitespace
        normalized = ' '.join(normalized.split())

        return normalized

    def title_similarity(self, title1: str, title2: str) -> float:
        """
        Calculate similarity between two titles.

        Args:
            title1: First title
            title2: Second title

        Returns:
            Similarity score (0-1)
        """
        norm1 = self.normalize_title(title1)
        norm2 = self.normalize_title(title2)

        if not norm1 or not norm2:
            return 0.0

        return SequenceMatcher(None, norm1, norm2).ratio()

    def deduplicate_by_doi(self, records: pd.DataFrame) -> pd.DataFrame:
        """
        Remove exact duplicates based on DOI.

        Args:
            records: DataFrame with 'doi' column

        Returns:
            Deduplicated DataFrame
        """
        logger.info(f"Starting with {len(records)} records")

        # Remove records without DOI first
        has_doi = records[records['doi'].notna() & (records['doi'] != '')]
        no_doi = records[records['doi'].isna() | (records['doi'] == '')]

        logger.info(f"Records with DOI: {len(has_doi)}")
        logger.info(f"Records without DOI: {len(no_doi)}")

        # Deduplicate by DOI
        before_dedup = len(has_doi)
        has_doi_dedup = has_doi.drop_duplicates(subset=['doi'], keep='first')
        doi_duplicates_removed = before_dedup - len(has_doi_dedup)

        logger.info(f"Removed {doi_duplicates_removed} DOI duplicates")

        # Combine back
        deduplicated = pd.concat([has_doi_dedup, no_doi], ignore_index=True)

        return deduplicated

    def deduplicate_by_title(self, records: pd.DataFrame) -> pd.DataFrame:
        """
        Remove fuzzy duplicates based on title similarity.

        Args:
            records: DataFrame with 'title' column

        Returns:
            Deduplicated DataFrame
        """
        if 'title' not in records.columns:
            logger.warning("No 'title' column found")
            return records

        logger.info(f"Fuzzy deduplication on {len(records)} records")

        # Track which records to keep
        keep_indices = []
        skip_indices = set()

        for i, row_i in records.iterrows():
            if i in skip_indices:
                continue

            keep_indices.append(i)

            # Compare with remaining records
            for j, row_j in records.iloc[i+1:].iterrows():
                if j in skip_indices:
                    continue

                similarity = self.title_similarity(row_i['title'], row_j['title'])

                if similarity >= self.title_similarity_threshold:
                    skip_indices.add(j)
                    logger.debug(f"Fuzzy duplicate found: {similarity:.2f} similarity")

        logger.info(f"Removed {len(skip_indices)} fuzzy title duplicates")

        deduplicated = records.loc[keep_indices].reset_index(drop=True)

        return deduplicated

    def merge_databases(self, database_files: List[Path],
                       database_names: List[str]) -> pd.DataFrame:
        """
        Merge records from multiple database exports.

        Args:
            database_files: List of paths to CSV files
            database_names: List of database names (same order as files)

        Returns:
            Merged DataFrame with source tracking
        """
        all_records = []

        for file_path, db_name in zip(database_files, database_names):
            logger.info(f"Loading {db_name}: {file_path}")

            df = pd.read_csv(file_path)
            self.validate_schema(df, db_name)
            df['source_database'] = db_name
            df['source_record_id'] = [f"{db_name}:{i+1}" for i in range(len(df))]
            df['lineage_ids'] = df['source_record_id']

            all_records.append(df)

            logger.info(f"  Loaded {len(df)} records from {db_name}")

        # Combine all records
        merged = pd.concat(all_records, ignore_index=True)

        logger.info(f"Total records before deduplication: {len(merged)}")

        return merged

    def generate_dedup_report(self, original_counts: Dict[str, int],
                            final_df: pd.DataFrame,
                            output_path: Path):
        """
        Generate deduplication report.

        Args:
            original_counts: Dictionary mapping database name to original count
            final_df: Final deduplicated DataFrame
            output_path: Path to save report
        """
        report_lines = [
            "DEDUPLICATION REPORT",
            "=" * 60,
            "",
            f"Report generated: {pd.Timestamp.now()}",
            "",
            "ORIGINAL COUNTS BY DATABASE",
            "-" * 60
        ]

        total_original = 0
        for db_name, count in original_counts.items():
            report_lines.append(f"{db_name}: {count:,} records")
            total_original += count

        report_lines.extend([
            "",
            f"Total records before deduplication: {total_original:,}",
            "",
            "AFTER DEDUPLICATION",
            "-" * 60,
            f"Unique records: {len(final_df):,}",
            f"Duplicates removed: {total_original - len(final_df):,}",
            f"Deduplication rate: {((total_original - len(final_df)) / total_original * 100):.1f}%",
            "",
            "LINEAGE",
            "-" * 60,
            "Each kept record carries source provenance in source_record_id and lineage_ids.",
            "",
            "SOURCES OF FINAL RECORDS",
            "-" * 60
        ])

        if 'source_database' in final_df.columns:
            source_counts = final_df['source_database'].value_counts()
            for source, count in source_counts.items():
                report_lines.append(f"{source}: {count:,} records")

        # Write report
        with open(output_path, 'w') as f:
            f.write('\n'.join(report_lines))

        logger.info(f"Deduplication report saved to {output_path}")


def main():
    """Main entry point for deduplication."""
    import argparse

    parser = argparse.ArgumentParser(description="Deduplicate and merge database search results")
    parser.add_argument('--inputs', nargs='+', required=True, help='Paths to input CSV files')
    parser.add_argument('--names', nargs='+', required=True, help='Database names (same order as inputs)')
    parser.add_argument('--output', required=True, help='Path to output merged CSV file')
    parser.add_argument('--report', default='dedup_report.txt', help='Path to deduplication report')
    parser.add_argument('--threshold', type=float, default=0.90, help='Title similarity threshold (0-1)')

    args = parser.parse_args()

    if len(args.inputs) != len(args.names):
        parser.error("Number of inputs must match number of names")

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Initialize deduplicator
    deduplicator = RecordDeduplicator(title_similarity_threshold=args.threshold)

    # Load and merge databases
    input_paths = [Path(p) for p in args.inputs]
    merged_df = deduplicator.merge_databases(input_paths, args.names)

    # Track original counts
    original_counts = dict(zip(args.names, [len(pd.read_csv(p)) for p in input_paths]))

    # Deduplicate by DOI
    merged_df = deduplicator.deduplicate_by_doi(merged_df)

    # Deduplicate by title
    merged_df = deduplicator.deduplicate_by_title(merged_df)

    # Save merged results
    merged_df.to_csv(args.output, index=False)
    logger.info(f"Merged and deduplicated results saved to {args.output}")

    # Generate report
    deduplicator.generate_dedup_report(
        original_counts,
        merged_df,
        Path(args.report)
    )


if __name__ == "__main__":
    main()
