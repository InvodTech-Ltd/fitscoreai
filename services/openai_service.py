import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze_resume_job(resume: str, job: str) -> dict:
    prompt = f"""
You are a professional job coach and hiring expert. Analyze the following resume and job description.

Resume:
\"\"\"{resume}\"\"\"

Job Description:
\"\"\"{job}\"\"\"

Evaluate the resume for the job and return a JSON with the following:
- match_score (0-100)
- missing_keywords: [string]
- suggestions: [string]
- summary: string
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response['choices'][0]['message']['content']
    return eval(content) if content.startswith("{") else {"error": "Invalid GPT response"}
