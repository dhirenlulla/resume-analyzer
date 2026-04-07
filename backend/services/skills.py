from backend.models.skill_list import SKILLS

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text.lower())
    skills = set()

    for token in doc:
        if token.text in SKILLS:
            skills.add(token.text)

    for chunk in doc.noun_chunks:
        if chunk.text in SKILLS:
            skills.add(chunk.text)

    return list(skills)