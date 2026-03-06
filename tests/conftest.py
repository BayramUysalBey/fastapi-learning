import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client



# Pytest automatically finds this file and makes its "fixtures" (like the client) accessible to any test file in that folder.