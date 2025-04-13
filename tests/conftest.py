import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure project root is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.main import app

client = TestClient(app)

@pytest.fixture
def auth_header():
    # Call the /token endpoint to get a valid token
    response = client.post("/token", data={"username": "test", "password": "test123"})
    token = response.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def test_client():
    return client
