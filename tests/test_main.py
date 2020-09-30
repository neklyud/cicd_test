import pytest
from fastapi import FastAPI
from app.helper import create_app
import requests

@pytest.fixture
def server_setup() -> FastAPI:
    yield create_app()

class TestClient:
    def test_get__success(self):
        resp = requests.get('http://localhost/')
        assert resp.status_code == 200        