import pdfplumber
import docx2txt
from fastapi import UploadFile
import os
import tempfile

async def extract_text_from_file(file: UploadFile) -> str:
    ext = os.path.splitext(file.filename)[1].lower()

    if ext == ".pdf":
        return await extract_pdf(file)
    elif ext == ".docx":
        return await extract_docx(file)
    elif ext == ".txt":
        contents = await file.read()
        return contents.decode("utf-8")
    else:
        raise ValueError("Unsupported file format: only .pdf, .docx, .txt allowed.")

async def extract_pdf(file: UploadFile) -> str:
    contents = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    text = ""
    with pdfplumber.open(tmp_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    os.remove(tmp_path)
    return text.strip()

async def extract_docx(file: UploadFile) -> str:
    contents = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    text = docx2txt.process(tmp_path)
    os.remove(tmp_path)
    return text.strip()
