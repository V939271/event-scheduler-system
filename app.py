from flask import Flask, request, jsonify
from utils import load_events, save_events, find_event_by_id
import uuid
from datetime import datetime
from reminder import check_reminders  
import threading

app = Flask(__name__)
events = load_events()

@app.route("/events", methods=["POST"]) # signature is /events { }
def create_event():
    data = request.get_json() # here request is read json body in postman
    event = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"]
    }
    events.append(event)
    save_events(events) # here we all call the save_events funtion and pass the events data and saved into file
    return jsonify({"message": "Event created", "event": event}), 201  # convert the dict data into json format

@app.route("/events", methods=["GET"])
def list_events():
    sorted_events = sorted(events, key=lambda x: x["start_time"]) # to Sort the data we used lambda fun
    return jsonify(sorted_events)

@app.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id): # to
    event = find_event_by_id(events, event_id) # this event is getting form api <event_id>
    if not event:
        return jsonify({"error": "Event not found"}), 404
    data = request.get_json()
    event.update({k: data[k] for k in ["title", "description", "start_time", "end_time"] if k in data})
    save_events(events)
    return jsonify({"message": "Event updated", "event": event})

@app.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    #global events
    events = [e for e in events if e["id"] != event_id] 
    save_events(events)
    return jsonify({"message": "Event deleted"}), 200

if __name__ == "__main__": 
    app.run(debug=True) # To run app 

reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()
