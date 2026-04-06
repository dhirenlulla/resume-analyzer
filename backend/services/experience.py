import re

def extract_experience(text):
    pattern = r"(\d+)\+?\s*(years|year)"
    matches = re.findall(pattern, text.lower())

    years = [int(m[0]) for m in matches]

    return max(years) if years else 0