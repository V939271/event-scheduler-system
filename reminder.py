import time
from datetime import datetime, timedelta
from utils import load_events

def check_reminders():
    while True:
        now = datetime.now()
        upcoming = []
        for event in load_events():
            start = datetime.strptime(event["start_time"], "%Y-%m-%d %H:%M")
            if now <= start <= now + timedelta(hours=1):
                upcoming.append(event)
        if upcoming:
            print("Upcoming Events in the next hour:")
            for e in upcoming:
                print(f"- {e['title']} at {e['start_time']}")
        time.sleep(60)  # Check every minute
