from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import openai_service

router = APIRouter()

class ScoreRequest(BaseModel):
    resume_text: str
    job_text: str

@router.post("/")
async def get_score(data: ScoreRequest):
    try:
        result = await openai_service.analyze_resume_job(data.resume_text, data.job_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
