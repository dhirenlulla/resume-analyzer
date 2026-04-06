from models.skill_list import SKILLS

def extract_job_skills(job_desc):
    job_desc = job_desc.lower()
    return [skill for skill in SKILLS if skill in job_desc]

def skill_gap_analysis(resume_skills, job_skills):
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    return {"matched": matched, "missing": missing}