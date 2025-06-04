# Update src/main.py to include report generation and email

from fetch_jobs.jsearch_api import fetch_jobs_jsearch
from fetch_jobs.indeed_scraper import fetch_jobs_indeed
from data.save_jobs import save_jobs_to_csv
from reports.generate_report import generate_pdf_report
from mailer.send_email import send_email_with_attachment
import os

def main():
    # Fetch jobs via API
    jobs_api = fetch_jobs_jsearch()
    save_jobs_to_csv(jobs_api, filename="src/data/jobs_api.csv")

    # Fetch jobs by scraping
    jobs_scrape = fetch_jobs_indeed()
    save_jobs_to_csv(jobs_scrape, filename="src/data/jobs_scrape.csv")

    # Combine jobs for report (example: jobs_api)
    report_file = generate_pdf_report(jobs_api)

    # Email the report
    recipient = os.getenv("EMAIL_ADDRESS")
    send_email_with_attachment(
        to_email=recipient,
        subject="Daily AI Software Engineer Job Report",
        body="Attached is the daily job report for AI Software Engineer roles.",
        attachment_path=report_file
    )
    print("Report generated and emailed successfully.")

if __name__ == "__main__":
    main()
