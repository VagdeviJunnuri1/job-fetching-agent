from fetch_jobs.jsearch_api import fetch_multiple_roles
from data.save_jobs import save_jobs_to_csv
from reports.generate_report import generate_pdf_report
from mailer.send_email import send_email_with_attachment
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🚀 Starting job-fetching agent...")

    roles = ["AI Engineer", "ML Engineer", "Software Engineer"]
    jobs = fetch_multiple_roles(roles, pages=3)

    # Sort by most recent first
    jobs.sort(key=lambda j: j.get("job_posted_at_timestamp", 0), reverse=True)

    job_count = len(jobs)
    print(f"✅ Fetched {job_count} jobs.")

    # Step 2: Save to CSV if any jobs exist
    if job_count:
        csv_path = "src/data/jobs.csv"
        save_jobs_to_csv(jobs, filename=csv_path)
        print(f"📄 Jobs saved to {csv_path}")
    else:
        print("⚠️ No jobs found. Skipping CSV.")

    # Step 3: Always generate PDF report
    report_path = "src/reports/job_report.pdf"
    generate_pdf_report(jobs, filename=report_path)
    print(f"📝 PDF report generated at {report_path}")

    # Step 4: Always email the report
    recipient = os.getenv("EMAIL_ADDRESS")
    subject = (
        f"📬 {job_count} New AI Software Jobs Today"
        if job_count
        else "❌ No New AI Software Jobs Today"
    )
    body = (
        "Hi,\n\n"
        "Please find today's job report attached.\n\n"
        "Note: No new jobs were found today." if not job_count else
        "Hi,\n\nPlease find today's job report attached.\n\nRegards,\nJob Agent"
    )

    send_email_with_attachment(
        to_email=recipient,
        subject=subject,
        body=body,
        attachment_path=report_path
    )
    print(f"📧 Report emailed to {recipient}")

if __name__ == "__main__":
    main()