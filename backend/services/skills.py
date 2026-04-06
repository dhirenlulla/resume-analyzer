import spacy
from backend.models.skill_list import SKILLS

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