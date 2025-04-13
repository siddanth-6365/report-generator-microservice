import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    user_payload = {
        "username": "newuser",
        "password": "newpass",
        "full_name": "New User"
    }
    response = client.post("/register", json=user_payload)
    assert response.status_code == 201, response.text

    response = client.post("/token", data={"username": "newuser", "password": "newpass"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data