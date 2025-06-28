from flask import Flask, request, jsonify
from utils import load_events, save_events, find_event_by_id
import uuid
from datetime import datetime

app = Flask(__name__)
events = load_events()

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    event = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"]
    }
    events.append(event)
    save_events(events)
    return jsonify({"message": "Event created", "event": event}), 201

@app.route("/events", methods=["GET"])
def list_events():
    sorted_events = sorted(events, key=lambda x: x["start_time"])
    return jsonify(sorted_events)

@app.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    event = find_event_by_id(events, event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    data = request.get_json()
    event.update({k: data[k] for k in ["title", "description", "start_time", "end_time"] if k in data})
    save_events(events)
    return jsonify({"message": "Event updated", "event": event})

@app.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    events = [e for e in events if e["id"] != event_id]
    save_events(events)
    return jsonify({"message": "Event deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
