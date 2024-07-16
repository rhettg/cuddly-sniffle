import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_review_get(client):
    response = client.get("/review")
    assert response.status_code == 200


# Add more tests as needed
