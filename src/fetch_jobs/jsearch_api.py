import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_multiple_roles(roles, pages=3):
    all_jobs = []

    for role in roles:
        print(f"🔍 Fetching role: {role}")
        for page in range(1, pages + 1):
            url = "https://jsearch.p.rapidapi.com/search"
            querystring = {
                "query": role,
                "location": "United States",
                "page": str(page),
                "num_pages": "1",
                "date_posted": "3days"
            }

            headers = {
                "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
                "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code == 200:
                jobs = response.json().get("data", [])
                all_jobs.extend(jobs)
                print(f"✅ {role} - Page {page}: {len(jobs)} jobs")
                if not jobs:
                    break
            else:
                print(f"❌ {role} - Page {page} failed")
                break

    return all_jobs
