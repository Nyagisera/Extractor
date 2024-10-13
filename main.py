import uvicorn
from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import JSONResponse, FileResponse
import os
from pdf_processing.pdf_extractor import process_large_batch_of_pdfs, search_pdfs
from nlp_tools.autocomplete import suggest_corrections

app = FastAPI()

# Path to save uploaded PDFs
UPLOAD_DIR = "./pdfs/"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename, "message": "PDF uploaded successfully"}

@app.get("/search-pdf/")
async def search_pdf(query: str = Query(...)):
    search_results = search_pdfs(query, UPLOAD_DIR)
    if not search_results:
        return JSONResponse(content={"error": "No matches found"}, status_code=404)

    return {"results": search_results}

@app.get("/autocomplete/")
async def autocomplete(query: str):
    suggestions = suggest_corrections(query)
    return {"suggestions": suggestions}

@app.get("/download-pdf/")
async def download_pdf(file: str):
    file_path = os.path.join(UPLOAD_DIR, file)
    if not os.path.exists(file_path):
        return JSONResponse(content={"error": "File not found"}, status_code=404)

    return FileResponse(file_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
