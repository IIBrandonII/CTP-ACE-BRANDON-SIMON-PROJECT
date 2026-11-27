from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_200():
    response = client.get("/api/v1/health")

    assert response.status_code == 200


def test_health_endpoint_returns_expected_payload():
    response = client.get("/api/v1/health")

    assert response.json() == {
        "status": "ok",
        "service": "ifms-api",
    }


def test_unknown_endpoint_returns_404():
    response = client.get("/api/v1/nonexistent")

    assert response.status_code == 404


def test_health_endpoint_rejects_post():
    response = client.post("/api/v1/health")

    assert response.status_code == 405
