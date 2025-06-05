from fpdf import FPDF
from pathlib import Path

def generate_pdf_report(jobs, filename="src/reports/job_report.pdf"):
    Path("src/reports").mkdir(parents=True, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Daily Job Report", ln=True, align="C")
    pdf.ln(10)

    if not jobs:
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "No jobs found for today.", ln=True)
    else:
        for job in jobs:
            title = job.get("job_title", "No Title")
            company = job.get("employer_name", "N/A")
            location = job.get("job_location", "N/A")
            link = job.get("job_apply_link", "No Link")

            pdf.set_font("Arial", "B", 12)
            pdf.multi_cell(0, 10, title)
            pdf.set_font("Arial", size=11)
            pdf.cell(0, 8, f"Company: {company}", ln=True)
            pdf.cell(0, 8, f"Location: {location}", ln=True)
            pdf.set_text_color(0, 0, 255)
            pdf.cell(0, 8, link, ln=True, link=link)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(6)

    pdf.output(filename)