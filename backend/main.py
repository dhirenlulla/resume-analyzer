from fastapi import FastAPI, UploadFile, File, Form
from backend.services.parser import extract_text_from_pdf
from backend.services.skills import extract_skills
from backend.services.ats import calculate_ats_score
from backend.services.sections import extract_sections
from backend.services.experience import extract_experience
from backend.services.matcher import extract_job_skills, skill_gap_analysis
from backend.services.scorer import resume_score_breakdown
from backend.services.llm import generate_suggestions

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), job_desc: str = Form(...)):
    content = await file.read()

    text = extract_text_from_pdf(content)

    skills = extract_skills(text)
    ats = calculate_ats_score(text, job_desc)
    sections = extract_sections(text)
    experience = extract_experience(text)

    job_skills = extract_job_skills(job_desc)
    gap = skill_gap_analysis(skills, job_skills)

    final_score = resume_score_breakdown(ats, len(skills), experience)

    suggestions = generate_suggestions(text)

    return {
        "ats_score": ats,
        "final_score": final_score,
        "skills": skills,
        "experience_years": experience,
        "sections": sections,
        "skill_gap": gap,
        "suggestions": suggestions
    }