import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RAPIDAPI_KEY")

def fetch_jobs_jsearch():
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": "Software Engineer",
        "page": "1",
        "num_pages": "1",
        "date_posted": "today",
        "remote_jobs_only": "true"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()["data"]