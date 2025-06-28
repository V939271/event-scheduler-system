import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_event(client):
    data = {
        "title": "Meeting",
        "description": "Team meeting",
        "start_time": "2025-07-01 10:00",
        "end_time": "2025-07-01 11:00"
    }
    response = client.post("/events", json=data)
    assert response.status_code == 201
