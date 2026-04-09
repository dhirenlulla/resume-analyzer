# 🚀 AI Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green" />
  <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img src="https://img.shields.io/badge/NLP-spaCy-orange" />
  <img src="https://img.shields.io/badge/ML-Transformers-yellow" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

An intelligent **AI-powered Resume Analyzer** that evaluates resumes against job descriptions using **NLP + Machine Learning**, generating ATS scores, skill gaps, and actionable suggestions.

---

## 🌟 Key Highlights (For Recruiters)

* 🔍 Built end-to-end NLP pipeline for resume parsing
* 📊 Designed ATS scoring logic using ML + heuristics
* 🧠 Integrated transformer-based semantic matching
* ⚡ FastAPI backend with modular service architecture

---

## 📌 Features

* 📄 Upload Resume (PDF)
* 🧠 NLP-based text extraction
* 🎯 ATS Score Calculation
* 🛠️ Skill Extraction
* 📊 Section Detection (Education, Experience, etc.)
* ⏳ Experience Estimation
* 🔍 Skill Gap Analysis vs Job Description
* 🤖 AI-generated Resume Improvement Suggestions

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **NLP:** spaCy
* **ML Models:** Transformers, Sentence Transformers
* **PDF Processing:** PyMuPDF
* **Data Handling:** Pandas, Scikit-learn

---

## 🧩 Architecture Overview

```
            ┌──────────────┐
            │  Resume PDF  │
            └──────┬───────┘
                   │
        ┌──────────▼──────────┐
        │  Text Extraction    │  (PyMuPDF)
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   NLP Processing    │  (spaCy)
        │  - Skills           │
        │  - Sections         │
        │  - Experience       │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   ML Matching       │  (Transformers)
        │  - JD Comparison    │
        │  - Skill Gap        │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │  Scoring Engine     │
        │  - ATS Score        │
        │  - Final Score      │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ AI Suggestions (LLM)│
        └──────────┬──────────┘
                   │
            ┌──────▼───────┐
            │   JSON API   │
            └──────────────┘
```

---

## 📁 Project Structure

```
backend/
│── main.py
│── services/
│   ├── parser.py
│   ├── skills.py
│   ├── ats.py
│   ├── sections.py
│   ├── experience.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── llm.py
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r ../requirements.txt
python -m spacy download en_core_web_sm
```

---

## ▶️ Run Locally

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 API Usage

### POST `/analyze`

**Request (cURL):**

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@resume.pdf" \
  -F "job_desc=Looking for a Python developer with ML experience"
```

**Response:**

```json
{
  "ats_score": 75,
  "final_score": 82,
  "skills": ["Python", "SQL"],
  "experience_years": 2,
  "sections": ["Education", "Experience"],
  "skill_gap": ["Docker", "AWS"],
  "suggestions": "Improve your resume by..."
}
```

---

## 🧠 How It Works

1. Extracts text from resume
2. Identifies skills and sections using NLP
3. Matches resume with job description
4. Computes ATS score
5. Detects missing skills
6. Generates improvement suggestions

---

## 📈 Future Improvements

* 🌐 Frontend (React / Streamlit)
* 📊 Advanced ML scoring model
* 🧾 Multi-format resume support
* ☁️ Cloud deployment (Railway / GCP)

---

## 👨‍💻 Author

**Dhiren Lulla**

---

## ⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!
