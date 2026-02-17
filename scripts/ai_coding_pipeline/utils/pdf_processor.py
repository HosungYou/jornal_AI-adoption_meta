#!/usr/bin/env python3
"""
PDF processing utilities for extracting text and tables.
Includes OCR fallback for scanned PDFs.
"""

import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import re

logger = logging.getLogger(__name__)


class PDFProcessor:
    """Handles PDF text extraction and table detection."""

    def __init__(self):
        """Initialize PDF processor."""
        # Try to import PDF libraries
        self.pdfplumber_available = False
        self.pypdf2_available = False
        self.tesseract_available = False

        try:
            import pdfplumber
            self.pdfplumber = pdfplumber
            self.pdfplumber_available = True
            logger.info("pdfplumber available")
        except ImportError:
            logger.warning("pdfplumber not available. Install with: pip install pdfplumber")

        try:
            import PyPDF2
            self.PyPDF2 = PyPDF2
            self.pypdf2_available = True
            logger.info("PyPDF2 available")
        except ImportError:
            logger.warning("PyPDF2 not available. Install with: pip install PyPDF2")

        try:
            import pytesseract
            from PIL import Image
            self.pytesseract = pytesseract
            self.Image = Image
            self.tesseract_available = True
            logger.info("pytesseract available for OCR")
        except ImportError:
            logger.warning("pytesseract not available. OCR will not work. Install with: pip install pytesseract pillow")

    def extract_text(self, pdf_path: Path) -> str:
        """
        Extract all text from a PDF.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted text
        """
        # Try pdfplumber first (better quality)
        if self.pdfplumber_available:
            try:
                return self._extract_with_pdfplumber(pdf_path)
            except Exception as e:
                logger.warning(f"pdfplumber extraction failed: {e}")

        # Fallback to PyPDF2
        if self.pypdf2_available:
            try:
                return self._extract_with_pypdf2(pdf_path)
            except Exception as e:
                logger.warning(f"PyPDF2 extraction failed: {e}")

        raise RuntimeError(f"Could not extract text from {pdf_path}. No PDF library available.")

    def _extract_with_pdfplumber(self, pdf_path: Path) -> str:
        """Extract text using pdfplumber."""
        text_parts = []

        with self.pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

        return '\n\n'.join(text_parts)

    def _extract_with_pypdf2(self, pdf_path: Path) -> str:
        """Extract text using PyPDF2."""
        text_parts = []

        with open(pdf_path, 'rb') as f:
            reader = self.PyPDF2.PdfReader(f)

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

        return '\n\n'.join(text_parts)

    def extract_tables(self, pdf_path: Path) -> List[List[List[str]]]:
        """
        Extract tables from PDF.

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of tables (each table is a list of rows)
        """
        if not self.pdfplumber_available:
            logger.warning("pdfplumber required for table extraction")
            return []

        all_tables = []

        try:
            with self.pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    if tables:
                        all_tables.extend(tables)

        except Exception as e:
            logger.error(f"Table extraction failed: {e}")

        return all_tables

    def extract_page_range(self, pdf_path: Path, start_page: int, end_page: int) -> str:
        """
        Extract text from specific page range.

        Args:
            pdf_path: Path to PDF file
            start_page: Starting page (1-indexed)
            end_page: Ending page (1-indexed, inclusive)

        Returns:
            Extracted text from page range
        """
        if self.pdfplumber_available:
            text_parts = []

            with self.pdfplumber.open(pdf_path) as pdf:
                for i in range(start_page - 1, min(end_page, len(pdf.pages))):
                    page_text = pdf.pages[i].extract_text()
                    if page_text:
                        text_parts.append(page_text)

            return '\n\n'.join(text_parts)

        elif self.pypdf2_available:
            text_parts = []

            with open(pdf_path, 'rb') as f:
                reader = self.PyPDF2.PdfReader(f)

                for i in range(start_page - 1, min(end_page, len(reader.pages))):
                    page_text = reader.pages[i].extract_text()
                    if page_text:
                        text_parts.append(page_text)

            return '\n\n'.join(text_parts)

        else:
            raise RuntimeError("No PDF library available")

    def find_correlation_tables(self, pdf_path: Path) -> List[Dict[str, Any]]:
        """
        Find tables that likely contain correlations.

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of candidate correlation tables with metadata
        """
        if not self.pdfplumber_available:
            logger.warning("pdfplumber required for table detection")
            return []

        correlation_tables = []

        # Keywords that indicate correlation tables
        keywords = [
            'correlation', 'correlations', 'pearson', 'spearman',
            'means', 'standard deviations', 'descriptive statistics',
            'intercorrelations'
        ]

        try:
            with self.pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    # Get page text
                    page_text = page.extract_text() or ""
                    page_text_lower = page_text.lower()

                    # Check if page mentions correlations
                    has_correlation_keyword = any(kw in page_text_lower for kw in keywords)

                    if has_correlation_keyword:
                        # Extract tables from this page
                        tables = page.extract_tables()

                        for table_idx, table in enumerate(tables):
                            if self._is_correlation_table(table):
                                correlation_tables.append({
                                    'page': page_num,
                                    'table_index': table_idx,
                                    'table_data': table,
                                    'confidence': 'high' if 'correlation' in page_text_lower else 'medium'
                                })

        except Exception as e:
            logger.error(f"Correlation table detection failed: {e}")

        return correlation_tables

    def _is_correlation_table(self, table: List[List[str]]) -> bool:
        """
        Heuristic check if a table is a correlation matrix.

        Args:
            table: Table data

        Returns:
            True if likely a correlation table
        """
        if not table or len(table) < 3:
            return False

        # Check if table has numeric values
        numeric_cells = 0
        total_cells = 0

        for row in table[1:]:  # Skip header
            for cell in row[1:]:  # Skip row labels
                if cell:
                    total_cells += 1
                    # Try to parse as float
                    try:
                        val = float(cell.strip().replace(',', '.'))
                        if -1 <= val <= 1:  # Correlation range
                            numeric_cells += 1
                    except ValueError:
                        pass

        # If >50% of cells are numeric in correlation range, likely a correlation table
        if total_cells > 0:
            numeric_ratio = numeric_cells / total_cells
            return numeric_ratio > 0.5

        return False

    def ocr_page(self, pdf_path: Path, page_num: int) -> str:
        """
        Perform OCR on a specific page (for scanned PDFs).

        Args:
            pdf_path: Path to PDF file
            page_num: Page number (1-indexed)

        Returns:
            OCR-extracted text
        """
        if not self.tesseract_available:
            raise RuntimeError("pytesseract required for OCR. Install with: pip install pytesseract pillow")

        try:
            # Convert PDF page to image
            from pdf2image import convert_from_path

            images = convert_from_path(
                pdf_path,
                first_page=page_num,
                last_page=page_num
            )

            if not images:
                return ""

            # Perform OCR
            text = self.pytesseract.image_to_string(images[0])

            return text

        except ImportError:
            logger.error("pdf2image required for OCR. Install with: pip install pdf2image")
            return ""
        except Exception as e:
            logger.error(f"OCR failed: {e}")
            return ""

    def get_metadata(self, pdf_path: Path) -> Dict[str, Any]:
        """
        Extract PDF metadata.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dictionary with metadata
        """
        metadata = {
            'filename': pdf_path.name,
            'file_size_bytes': pdf_path.stat().st_size
        }

        if self.pdfplumber_available:
            try:
                with self.pdfplumber.open(pdf_path) as pdf:
                    metadata['n_pages'] = len(pdf.pages)
                    metadata['pdf_metadata'] = pdf.metadata
            except Exception as e:
                logger.warning(f"Failed to extract metadata with pdfplumber: {e}")

        elif self.pypdf2_available:
            try:
                with open(pdf_path, 'rb') as f:
                    reader = self.PyPDF2.PdfReader(f)
                    metadata['n_pages'] = len(reader.pages)
                    metadata['pdf_metadata'] = reader.metadata
            except Exception as e:
                logger.warning(f"Failed to extract metadata with PyPDF2: {e}")

        return metadata


def test_pdf_processor():
    """Test PDF processor functionality."""
    print("Testing PDF processor...\n")

    processor = PDFProcessor()

    print("1. Checking available libraries:")
    print(f"   pdfplumber: {processor.pdfplumber_available}")
    print(f"   PyPDF2: {processor.pypdf2_available}")
    print(f"   pytesseract: {processor.tesseract_available}")

    # Note: Actual file testing would require a PDF file
    print("\n2. PDF processor initialized successfully")
    print("   Ready to process PDFs")

    print("\nAvailable methods:")
    print("   - extract_text()")
    print("   - extract_tables()")
    print("   - extract_page_range()")
    print("   - find_correlation_tables()")
    print("   - ocr_page() [if pytesseract available]")
    print("   - get_metadata()")


if __name__ == "__main__":
    test_pdf_processor()
