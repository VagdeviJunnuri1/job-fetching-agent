import requests
from bs4 import BeautifulSoup

def fetch_jobs_indeed():
    url = "https://www.indeed.com/jobs?q=software+engineer&l=remote&fromage=1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("a", class_="tapItem")
    jobs = []

    for card in job_cards:
        title = card.find("h2", class_="jobTitle").text.strip()
        company = card.find("span", class_="companyName").text.strip()
        location = card.find("div", class_="companyLocation").text.strip()
        link = "https://www.indeed.com" + card["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    return jobs
