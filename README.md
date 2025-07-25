
# 🧠 FitScore AI

**"Optimize Your Resume. Maximize Your Chances."**

FitScore AI is an AI-powered web application that helps users analyze how well their resume matches a job description. By leveraging OpenAI GPT-4, it generates a match score, a concise explanation, and personalized suggestions for improvement.

---

## 📌 Features

- Upload resume and job description files (.pdf, .docx, .txt)
- Extract and clean text using Python parsers
- Evaluate match with GPT-4 and return:
  - A score (0–100)
  - An explanation
  - Three improvement tips
- Responsive UI for a smooth experience

---

## 🧱 Tech Stack

| Layer        | Technology                |
|--------------|----------------------------|
| **Frontend** | React + Tailwind CSS (or Flutter Web) |
| **Backend**  | Python + FastAPI           |
| **AI/NLP**   | OpenAI GPT-4 API           |
| **Parsing**  | `pdfplumber`, `docx2txt`   |
| **Deployment** | Vercel (Frontend), Render or Heroku (Backend) |

---

## 🧠 System Architecture

```
[User] 
  |
  v
[Frontend (React/Flutter)]
  |
  v
[FastAPI Backend]
  |- Text Parser (PDF/DOCX/TXT)
  |- Prompt Builder
  |- GPT-4 Evaluator
  |
  v
[OpenAI API]
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fitscore-ai.git
cd fitscore-ai
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Backend Server
```bash
uvicorn main:app --reload
```

---

## 📂 API Endpoints

### `POST /upload`
**Uploads resume and job files.**

- **Request:** `multipart/form-data`
  - `resume`: File (.pdf, .docx, .txt)
  - `job`: File (.pdf, .docx, .txt)

- **Response:**
```json
{
  "resume_text": "Extracted resume text...",
  "job_text": "Extracted job text..."
}
```

---

### `POST /score`
**Submits text for GPT-4 scoring.**

- **Request:**
```json
{
  "resume_text": "text string",
  "job_text": "text string"
}
```

- **Response:**
```json
{
  "score": 85,
  "explanation": "You match 90% of required skills...",
  "suggestions": [
    "Include more cloud experience.",
    "Add quantifiable project outcomes.",
    "Use keywords from the job post."
  ]
}
```

---

## 📄 GPT Prompt Template

```plaintext
You are an AI career advisor. Given the following resume and job description, evaluate how well the resume matches the job.

Return:
1. A match score (0–100)
2. A short explanation
3. Three resume improvement suggestions

Respond in JSON format:
{
  "score": <int>,
  "explanation": "<reasoning>",
  "suggestions": ["...", "...", "..."]
}
```

---

## 📁 Project Structure

```
fitscore-ai/
├── main.py
├── routers/
│   ├── upload.py
│   └── score.py
├── services/
│   ├── extractor.py
│   └── openai_service.py
├── utils/
│   └── file_utils.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

- ✅ Unit tests for parsers
- ✅ Integration testing for upload → score pipeline
- ✅ Handle invalid file formats gracefully

---

## 🔄 Roadmap

- [ ] Frontend UI
- [ ] Resume keyword highlighter
- [ ] User accounts + resume history
- [ ] AI resume rewriter
- [ ] LinkedIn/Indeed import

---

## 📄 License

MIT License © 2025 [Your Name]

---

## 🙌 Acknowledgments

- [OpenAI GPT-4](https://platform.openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [docx2txt](https://github.com/ankushshah89/python-docx2txt)

---

## ✉️ Contact

Built by [@yourusername](https://github.com/yourusername)  
Feel free to fork, contribute, or open an issue!
