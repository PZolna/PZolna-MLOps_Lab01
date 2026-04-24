from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root_route_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_route_returns_ok_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
