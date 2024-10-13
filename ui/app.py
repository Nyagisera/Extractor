from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
import os
from pdf_processor import process_pdf, search_in_pdf

app = FastAPI()

PDF_DIRECTORY = "./pdfs/"

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(PDF_DIRECTORY, file.filename)
    with open(file_location, "wb+") as f:
        f.write(file.file.read())
    return {"message": "PDF uploaded successfully", "filename": file.filename}

@app.post("/search/")
async def search_pdf(query: str = Form(...), filename: str = Form(...)):
    file_location = os.path.join(PDF_DIRECTORY, filename)
    if os.path.exists(file_location):
        results = search_in_pdf(query, file_location)
        return JSONResponse(content=results)
    return {"error": "File not found"}

@app.get("/download/{filename}")
async def download_pdf(filename: str):
    file_path = os.path.join(PDF_DIRECTORY, filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename)
    return {"error": "File not found"}
