import pytest
import requests

@pytest.fixture(scope="session")
def api_base_url():
    return "https://dummyjson.com"

@pytest.fixture()
def api():
    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "qa-shopito/1.0"
    })
    yield s
    s.close()
