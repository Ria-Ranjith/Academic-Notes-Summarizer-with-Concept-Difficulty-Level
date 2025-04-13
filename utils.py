from PyPDF2 import PdfReader  # Using PyPDF2 instead of pdfminer for consistency
import docx
from typing import Union, IO


def extract_text_from_pdf(file: Union[str, IO[bytes]]) -> str:
    """Extracts text from PDFs using PyPDF2 (matches your requirements.txt).
    
    Args:
        file: File path (str) or file object (BytesIO)
    
    Returns:
        Extracted text as string. Empty string if extraction fails.
    """
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Handle None returns
        return text.strip()
    except Exception as e:
        raise RuntimeError(f"PDF read failed: {str(e)}")


def extract_text_from_docx(file: Union[str, IO[bytes]]) -> str:
    """Extracts text from DOCX files using python-docx.
    
    Args:
        file: File path (str) or file object (BytesIO)
    
    Returns:
        Text as newline-separated string. Empty if fails.
    """
    try:
        doc = docx.Document(file)
        return '\n'.join(
            paragraph.text 
            for paragraph in doc.paragraphs 
            if paragraph.text.strip()  # Skip empty paragraphs
        )
    except Exception as e:
        raise RuntimeError(f"DOCX read failed: {str(e)}")

