#  Event Scheduler System

A simple Python Flask-based REST API that allows users to add, view, update, and delete scheduled events. All events are saved to a local JSON file for persistence.

---

##  Technologies Used

- **Language**: Python 3.x
- **Framework**: Flask
- **API Type**: REST
- **Testing Tool**: Postman
- **Optional**: Pytest for unit testing

---

##  Features

-  Create, read, update, and delete events
-  Persistent storage using `events.json`
-  Reminders for upcoming events (within 1 hour) – optional
-  API testing with Postman
-  (Optional) Support for recurring events

---

##  Project Structure

event-scheduler-system/
│
├── app.py # Main Flask API
├── utils.py # Helper functions and data handling
├── reminder.py # (Optional) Event reminders
├── test_app.py # (Optional) Unit tests with Pytest
├── events.json # Stores all event data
├── requirements.txt # Dependencies
└── README.md # Project instructions and examples


##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/V939271/event-scheduler-system.git
cd event-scheduler-system



## 2. Create and Activate Virtual Environment (Windows)

    python -m venv venv
    .\venv\Scripts\activate  # On Windows

## 3.  Install Dependencies

    pip install -r requirements.txt

## 4. Running the Application

    python app.py
    You should see output like:
    Running on http://127.0.0.1:5000/ 

## API Endpoints (with Postman Examples)


    # 1. Create Event
        POST /events
        Body (JSON):

    {
  "title": "Doctor Appointment",
  "description": "Visit Dr. Smith",
  "start_time": "2025-07-01 10:00",
  "end_time": "2025-07-01 11:00"
    }

        ## Sample Response:
                {
            "message": "Event created",
            "event": {
                "id": "004e959c-20a0-41fe-9dbc-71d9b2d8e52f",
                "title": "Doctor Appointment",
                "description": "Visit Dr. Smith",
                "start_time": "2025-07-01 10:00",
                "end_time": "2025-07-01 11:00"
                       }
                }

## 2. View All Events
    GET /events

    ## Sample Response:
                [
                    {
            "id": "004e959c-20a0-41fe-9dbc-71d9b2d8e52f",
            "title": "Doctor Appointment",
            "description": "Visit Dr. Smith",
            "start_time": "2025-07-01 10:00",
            "end_time": "2025-07-01 11:00"
                    }
                ]   

     



## 3. Update Event
    PUT /events/<event_id>
    Body (JSON):

                {
            "title": "Dentist Appointment",
            "description": "Teeth cleaning",
            "start_time": "2025-07-01 09:00",
            "end_time": "2025-07-01 10:00"
                }

## 4. Delete Event
    DELETE /events/<event_id>


## Run Tests 
    pytest test_app.py

## GitHub Repository
=> https://github.com/V939271/event-scheduler-system

## License

  Licensed under the MIT License

      
        



