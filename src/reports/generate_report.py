# src/reports/generate_report.py
from fpdf import FPDF

def generate_pdf_report(jobs, filename="src/reports/job_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Daily Job Report", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    for job in jobs:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, job.get("title", "No Title"), ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"Company: {job.get('company', 'N/A')}", ln=True)
        pdf.cell(0, 8, f"Location: {job.get('location', 'N/A')}", ln=True)
        pdf.set_text_color(0, 0, 255)
        pdf.cell(0, 8, job.get("link", "No Link"), ln=True, link=job.get("link", ""))
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)

    pdf.output(filename)
    return filename
