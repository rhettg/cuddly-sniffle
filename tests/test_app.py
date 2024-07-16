import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_data(monkeypatch):
    mock_documents = [{"id": 1, "content": "Test document"}]
    mock_questions = ["Test question"]
    mock_tags = ["Tag1", "Tag2"]

    def mock_load_data():
        return {
            "documents": mock_documents,
            "questions": mock_questions,
            "tags": mock_tags,
        }

    monkeypatch.setattr("app.load_data", mock_load_data)
    monkeypatch.setattr("app.documents", mock_documents)
    monkeypatch.setattr("app.questions", mock_questions)
    monkeypatch.setattr("app.tags", mock_tags)


@pytest.fixture
def mock_save_result(monkeypatch):
    def mock_save(result):
        # Do nothing, just a mock
        pass

    monkeypatch.setattr("app.save_result", mock_save)


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_review_get(client, mock_data):
    with client.session_transaction() as sess:
        sess["current_index"] = 0

    response = client.get("/review")
    assert response.status_code == 200


def test_review_post(client, mock_data, mock_save_result):
    with client.session_transaction() as sess:
        sess["current_index"] = 0

    response = client.post("/review", data={"tag": "Tag1"})
    assert response.status_code == 302  # Redirect after POST
    assert response.location == "/review"


# Add more tests as needed
