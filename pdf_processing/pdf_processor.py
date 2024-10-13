import PyPDF2
from pdf2image import convert_from_path
import re

def process_pdf(file_path):
    """Extracts text and images from the PDF."""
    text_content = ""
    images = []

    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            text_content += reader.getPage(page_num).extract_text()
        images = convert_from_path(file_path)  # Extract images

    return {"text": text_content, "images": images}

def search_in_pdf(query, file_path):
    """Searches the query in the PDF and returns matches."""
    text_data = process_pdf(file_path)["text"]
    matches = re.findall(query, text_data, re.IGNORECASE)
    return {"matches": matches, "total": len(matches)}
