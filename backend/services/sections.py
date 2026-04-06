def extract_sections(text):
    sections = {
        "education": "",
        "experience": "",
        "skills": "",
        "projects": ""
    }

    current = None

    for line in text.split("\n"):
        l = line.lower()

        if "education" in l:
            current = "education"
        elif "experience" in l:
            current = "experience"
        elif "skills" in l:
            current = "skills"
        elif "project" in l:
            current = "projects"

        elif current:
            sections[current] += line + "\n"

    return sections