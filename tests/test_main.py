from main import app
import pytest


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the index route."""
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    """Test the index route."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "UP"}
