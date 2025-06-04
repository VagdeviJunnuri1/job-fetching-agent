import csv
from pathlib import Path

def save_jobs_to_csv(jobs, filename="src/data/jobs.csv"):
    Path("src/data").mkdir(parents=True, exist_ok=True)
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "location", "link"])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
