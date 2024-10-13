This project is a web-based application that allows users to upload PDF files, search for specific text or images within them, and extract the results. It provides a user-friendly interface for previewing search results before downloading them, with an advanced search capability that includes features like autocomplete and spell correction.

## Features

1. **Upload PDFs**: Users can upload one or multiple PDF files to the system.
2. **Search within PDFs**: A powerful search functionality that allows users to search for any text or image within the uploaded PDFs.
   - **Advanced Search**: Supports auto-completion and spell correction.
   - **Text and Image Search**: Capable of extracting both text and images.
3. **Preview Results**: Users can preview the search results in the browser before downloading.
4. **Download Extracted Data**: Once the desired content is found, users can download the results as a new PDF file.
5. **Supports Multiple Formats**: Upload and preview PDFs, videos, audio, and URLs.
6. **Voice Search**: Integrated voice search option with mic support for easier queries.
7. **Modern UI**: Built with Bootstrap and a clean, responsive interface.

## Table of Contents

- [Demo](#demo)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [File Structure](#file-structure)
- [Credits](#credits)

## Demo

You can see the live demo of this project (if hosted) here: [DEMO LINK](#)

## Technologies

- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Backend**: Python (FastAPI)
- **Libraries**:
  - PyPDF2
  - pdf2image
  - pdfplumber (for advanced PDF processing)
  - FuzzyWuzzy (for autocomplete and spell correction)
  - Typeahead.js (for frontend auto-completion)

## Installation

Follow the steps below to install and run the project locally.

### Prerequisites

- Python 3.7 or above
- Node.js and npm (for managing frontend dependencies)

### Clone the repository

```bash
git clone https://github.com/your-username/pdf-search-extraction.git
cd pdf-search-extraction
```

### Backend Setup

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the FastAPI server:

    ```bash
    uvicorn app:app --reload
    ```

   The backend should now be running at `http://127.0.0.1:8000`.

### Frontend Setup

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Open the `index.html` file in your browser or use a local server (like `http-server`):

    ```bash
    npx http-server
    ```

   The frontend should now be running at `http://127.0.0.1:8080`.

## Usage

1. **Upload PDFs**: Drag and drop or select PDF files to upload.
2. **Search PDFs**: Enter a search query or use the microphone icon for voice search. The system will search through the uploaded PDFs and display matches in the preview section.
3. **Preview Results**: Results will be displayed in the preview section with both text and image highlights.
4. **Download Extracted Data**: Once you're satisfied with the search results, click the "Download" button to download the extracted data as a new PDF.

### API Endpoints

Here are the key API endpoints provided by the backend:

- `POST /upload/`: Uploads a PDF to the system.
- `POST /search/`: Searches for a specific query in the uploaded PDF.
- `GET /download/{filename}`: Downloads the extracted results as a PDF.

## File Structure

```
pdf-search-extraction/
│
├── backend/
│   ├── app.py            # FastAPI app (handles search and download functionality)
│   ├── pdf_processor.py   # Processes PDF data (extracts text and images)
│   ├── requirements.txt   # Python dependencies
│   └── pdfs/              # Directory where uploaded PDFs are stored
│
├── frontend/
│   ├── index.html         # Main frontend file
│   ├── script.js          # JavaScript logic for search, preview, and download
│   ├── styles.css         # CSS for the frontend
│   └── assets/            # Directory for static files (images, icons, etc.)
```

## Credits

- [PyPDF2](https://github.com/py-pdf/PyPDF2): For PDF text extraction.
- [pdf2image](https://github.com/Belval/pdf2image): For converting PDFs to images.
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy): For string matching and spell correction.
- [Typeahead.js](https://github.com/twitter/typeahead.js): For frontend auto-completion.
- [Bootstrap](https://getbootstrap.com/): For responsive UI components.

