import os
import sys
from dotenv import load_dotenv

load_dotenv()

os.environ["DATABASE_URL"] = os.getenv("DATABASE_URL")

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="session")
def test_client():
    return client

@pytest.fixture(scope="session")
def auth_header(test_client):
    # register a test user (here ignore error if already exists)
    user_payload = {
        "username": "testuser",
        "password": "testpass",
        "full_name": "Test User"
    }
    _ = test_client.post("/register", json=user_payload)
    
    response = test_client.post("/token", data={"username": "testuser", "password": "testpass"})
    token = response.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}
