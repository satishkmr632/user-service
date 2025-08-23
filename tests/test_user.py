from fastapi.testclient import TestClient
from src.user_service.main import app

client = TestClient(app)

def test_root():
    response = client.get("users/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World..1"}
