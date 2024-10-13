async function uploadPDF() {
    const fileInput = document.getElementById('pdfUpload');
    const files = fileInput.files;

    for (let i = 0; i < files.length; i++) {
        const formData = new FormData();
        formData.append('file', files[i]);

        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data.message);
    }
}

async function searchPDF() {
    const query = document.getElementById('searchQuery').value;
    const formData = new FormData();
    formData.append('query', query);
    formData.append('filename', "example.pdf"); // Assume example.pdf is uploaded

    const response = await fetch('/search/', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    displayResults(result);
}

function displayResults(data) {
    const previewContainer = document.getElementById('previewContainer');
    previewContainer.innerHTML = ""; // Clear previous results

    data.matches.forEach(match => {
        const div = document.createElement('div');
        div.innerHTML = `<p>${match}</p>`;
        previewContainer.appendChild(div);
    });
}

async function downloadPDF() {
    const response = await fetch(`/download/example_output.pdf`);
    if (response.ok) {
        const blob = await response.blob();
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'extracted_data.pdf';
        link.click();
    } else {
        console.error('Failed to download PDF');
    }
}