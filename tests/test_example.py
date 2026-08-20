import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5

def test_site_is_available():
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    assert response.status_code == 200

def test_has_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    data = response.json()
    assert len(data) > 0

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data