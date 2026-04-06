from fpdf import FPDF

def generate_report(data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Resume Analysis Report", ln=True)

    pdf.cell(200, 10, f"ATS Score: {data['ats_score']}", ln=True)
    pdf.cell(200, 10, f"Experience: {data['experience_years']}", ln=True)

    pdf.multi_cell(0, 10, "Skills: " + ", ".join(data["skills"]))
    pdf.multi_cell(0, 10, "Suggestions: " + data["suggestions"])

    file_path = "report.pdf"
    pdf.output(file_path)

    return file_path