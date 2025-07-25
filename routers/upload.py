from fastapi import APIRouter, File, UploadFile, HTTPException
from services import extractor

router = APIRouter()

@router.post("/")
async def upload_files(resume: UploadFile = File(...), job: UploadFile = File(...)):
    if not resume.filename or not job.filename:
        raise HTTPException(status_code=400, detail="Both files are required.")

    try:
        resume_text = await extractor.extract_text_from_file(resume)
        job_text = await extractor.extract_text_from_file(job)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process files: {e}")

    return {
        "resume_text": resume_text[:1000],  # Return preview (limit to 1000 chars)
        "job_text": job_text[:1000]
    }
