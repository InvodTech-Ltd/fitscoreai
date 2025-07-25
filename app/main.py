# type: ignore
from fastapi import FastAPI
from routers import upload, score 

app = FastAPI(
    title="FitScore AI",
    description="Analyze how well a resume matches a job description using AI",
    version="1.0.0"
)

# Register routers
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(score.router, prefix="/score", tags=["Score"])

@app.get("/")
def root():
    return {"message": "Welcome to FitScore AI! Upload your resume and job description to get started."}
