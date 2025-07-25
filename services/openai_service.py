import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # Optional: safely parse JSON (instead of eval)
    import json
    try:
        return json.loads(content)
    except:
        return {"response": content}
