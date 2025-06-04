# src/scheduler.py
import schedule
import time
from src.main import main

def job():
    print("Running daily job fetching and reporting...")
    main()

schedule.every().day.at("07:00").do(job)  # Set your preferred time here (24h format)

if __name__ == "__main__":
    print("Scheduler started, waiting for the daily job...")
    while True:
        schedule.run_pending()
        time.sleep(30)
