import json
import os

FILE_PATH = "events.json"

def load_events():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_events(events):
    with open(FILE_PATH, "w") as f:
        json.dump(events, f, indent=4)

def find_event_by_id(events, event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    return None
