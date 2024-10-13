from multiprocessing import Pool
from pdf_processing.pdf_extractor import extract_pdf_data

def parallel_process_pdfs(pdf_list, batch_size=20):
    """
    Function to handle large PDF processing using multiprocessing.
    """
    results = []
    with Pool() as pool:
        for i in range(0, len(pdf_list), batch_size):
            batch_files = pdf_list[i:i + batch_size]
            result = pool.map(extract_pdf_data, batch_files)
            results.extend(result)
    return results
