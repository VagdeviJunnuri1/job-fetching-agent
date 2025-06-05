import requests
import os
import json

def test_fetch_jobs():
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": "software engineer",
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    if not headers["X-RapidAPI-Key"]:
        print("❌ Missing RAPID_API_KEY in environment variables.")
        return

    try:
        response = requests.get(url, headers=headers, params=querystring)
        print(f"🔎 Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            jobs = data.get("data", [])
            print(f"✅ Total Jobs Fetched: {len(jobs)}")
            if jobs:
                print("📌 First Job Sample:")
                print(json.dumps(jobs[0], indent=2))
            else:
                print("⚠️ No jobs found in the response.")
        else:
            print("❌ Error Message:", response.text)

    except Exception as e:
        print("💥 Exception occurred while fetching jobs:", str(e))

if __name__ == "__main__":
    test_fetch_jobs()
