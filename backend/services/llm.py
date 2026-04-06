from transformers import pipeline

# Stable + fast model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def generate_suggestions(text):
    prompt = f"""
You are a professional resume reviewer.

Give 5 clear bullet point suggestions to improve the resume.

ONLY return bullet points.
DO NOT repeat the question.
DO NOT explain anything.

Resume:
{text[:400]}
"""

    try:
        result = generator(
            prompt,
            max_length=150,
            do_sample=False
        )

        output = result[0]["generated_text"].strip()

        # 🔥 CLEANING LOGIC
        lines = output.split("\n")
        cleaned = []

        for line in lines:
            line = line.strip()

            # Keep only meaningful bullet lines
            if len(line) > 10 and not line.lower().startswith("resume"):
                cleaned.append(line)

        # 🔥 FALLBACK (CRITICAL)
        if len(cleaned) < 2:
            return [
                "Add measurable achievements (e.g., improved accuracy by 20%)",
                "Include more relevant technical skills based on job description",
                "Use strong action verbs like 'developed', 'implemented'",
                "Structure projects with problem → solution → impact",
                "Optimize resume for ATS keywords"
            ]

        return cleaned

    except Exception as e:
        return [
            "Add measurable achievements",
            "Improve formatting and structure",
            "Include relevant technical skills",
            "Use action verbs",
            "Tailor resume to job description"
        ]