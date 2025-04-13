from pdfminer.high_level import extract_text
import docx
from typing import Union, IO
import warnings

def extract_text_from_pdf(file: Union[str, IO[bytes]]) -> str:
    """
    Extracts text from a PDF file.
    
    Args:
        file: Either a file path (str) or a file-like object (BytesIO).
    
    Returns:
        Extracted text as a string.
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Suppress PDFMiner warnings
            text = extract_text(file)
        return text.strip() if text else ""
    except Exception as e:
        raise RuntimeError(f"Failed to extract PDF text: {str(e)}")

def extract_text_from_docx(file: Union[str, IO[bytes]]) -> str:
    """
    Extracts text from a DOCX file.
    
    Args:
        file: Either a file path (str) or a file-like object (BytesIO).
    
    Returns:
        Extracted text as a string.
    """
    try:
        doc = docx.Document(file)
        return '\n'.join(para.text for para in doc.paragraphs if para.text.strip())
    except Exception as e:
        raise RuntimeError(f"Failed to extract DOCX text: {str(e)}")
