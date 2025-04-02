import pytest
import requests

@pytest.fixture
def api_client():
    base_url = "https://httpbin.org"  # Можно заменить на свой API
    return base_url
