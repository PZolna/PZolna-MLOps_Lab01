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


def test_predict_route_returns_prediction():
    request_body = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    response = client.post("/predict", json=request_body)

    assert response.status_code == 200
    assert response.json()["prediction"] in ["setosa", "versicolor", "virginica"]
