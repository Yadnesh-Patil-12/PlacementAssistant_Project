"""
utils/resume_parser.py
Extract text from PDF and save uploaded files.
"""

from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a text-based PDF.

    Returns:
        Extracted text as a string.
        Returns an empty string if extraction fails.
    """

    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        print(f"PDF Error: {e}")
        return ""


def save_uploaded_file(uploaded_file, save_path: str) -> str:
    """
    Save the uploaded PDF to disk.

    Args:
        uploaded_file: Streamlit UploadedFile object
        save_path: Destination file path

    Returns:
        Path where the file was saved
    """

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path