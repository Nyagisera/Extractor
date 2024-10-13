import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

# Extract text from PDFs
def extract_pdf_text(pdf_file):
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Search for text or images in PDFs
def search_pdfs(query, directory):
    pdf_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".pdf")]
    results = []

    for pdf_file in pdf_files:
        text = extract_pdf_text(pdf_file)
        if query.lower() in text.lower():
            results.append({
                "file": os.path.basename(pdf_file),
                "excerpt": get_excerpt(text, query)
            })
    
    return results

def get_excerpt(text, query):
    # Simple function to extract a few words around the query
    query_start = text.lower().find(query.lower())
    start = max(query_start - 30, 0)
    end = min(query_start + 30, len(text))
    return text[start:end] + '...'

# Extract images from PDFs
def extract_images(pdf_file):
    images = convert_from_path(pdf_file)
    return images
