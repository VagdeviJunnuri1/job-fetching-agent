# src/data/save_jobs.py
import csv
import os

def save_jobs_to_csv(jobs, filename):
    if not jobs:
        print("No jobs to save.")
        return

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = jobs[0].keys()  # dynamically get fieldnames from first job
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

