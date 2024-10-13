from fastapi import FastAPI, UploadFile, File
from pdf_processing.pdf_extractor import process_large_batch_of_pdfs
from pdf_processing.report_generator import generate_report
import os

app = FastAPI()

UPLOAD_DIR = "./uploads"

@app.post("/upload-files/")
async def upload_files(files: list[UploadFile] = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    pdf_files = []
    for file in files:
        file_location = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        pdf_files.append(file_location)

    extracted_data = process_large_batch_of_pdfs(UPLOAD_DIR)

    report_path = generate_report(extracted_data, output_format="docx")

    return {"message": "Files uploaded and processed successfully", "report": report_path}
