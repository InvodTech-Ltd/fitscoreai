from traceback import extract_tb
import pdfplumber
import docx2txt
from fastapi import UploadFile
import os

async def extract_text_from_file(file: UploadFile) -> str:
    ext = os.path.splitext(file.filename)[1].lower()

    if ext == ".pdf":
        return await extract_tb(file)
    elif ext == ".docx":
        return await extract_docx(file)
    elif ext == ".txt":
        return (await file.read()).decode("utf-8")
    else:
        raise ValueError("Unsupported file format: only .pdf, .docx, .txt allowed.")

async def extract_pdf(file: UploadFile) -> str:
    text = ""
    contents = await file.read()
    with open("/tmp/temp.pdf", "wb") as temp_file:
        temp_file.write(contents)
    with pdfplumber.open("/tmp/temp.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

async def extract_docx(file: UploadFile) -> str:
    contents = await file.read()
    with open("/tmp/temp.docx", "wb") as temp_file:
        temp_file.write(contents)
    return docx2txt.process("/tmp/temp.docx").strip()
