
# 🤖 FitScore AI

**Slogan:** _"Find your fit, smart and quick."_

FitScore AI is a smart, machine learning-powered API platform that evaluates how well a resume matches a job description. Designed to be completely self-hosted and cost-effective, it uses NLP and ML to score compatibility, identify skill gaps, and offer improvement suggestions — without relying on paid AI APIs.

---

## 🚀 Features

- 📄 Upload resume and job description (text or file)
- 🔍 NLP-based text analysis
- 📈 Predict a **fit score (0–100%)**
- 🧠 Highlight **missing keywords and suggestions**
- 🛠️ Fully local and open-source — no OpenAI, no billing
- 🌐 Host as a public API using FastAPI

---

## 🛠️ Tech Stack

| Layer         | Tools                            |
|---------------|----------------------------------|
| Language       | Python 3.10+                     |
| ML/NLP         | scikit-learn, spaCy, TF-IDF      |
| API Framework  | FastAPI, Uvicorn                 |
| Model Export   | joblib / pickle                  |
| Deployment     | Hugging Face Spaces / Railway / Render |
| Optional Frontend | React, Tailwind (planned)     |

---

## 📂 Project Structure

```
fitscore-ai/
├── main.py
├── model.py
├── schemas.py
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

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fitscoreai.git
cd fitscoreai
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Train the model

```bash
python app/ml/train_model.py
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

### 6. Open in Browser

```bash
Go to: http://localhost:8000/docs
```

---

---

## 🧪 Testing

- Use Swagger UI at /docs or Postman to test:

- Sample job descriptions

- Sample resume content

- Scoring endpoint

---

## 🔄 Roadmap

- Add transformer embeddings for deeper context

- Auto-extract skills from resumes (NER)

- Build web-based UI dashboard (React)

- Batch scoring for HR/recruiters

- Account system and scoring history

---

## 📄 License

MIT License © 2025 [Trevor Madara Kayeyia]

---

---

## ✉️ Contact

Built by [@Trevor-Kayeyia-Madara](https://github.com/Trevor-Kayeyia-Madara)  
Feel free to fork, contribute, or open an issue!
