import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5

def test_api_get_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_api_create_post():
    new_post = {"title": "QA Test", "body": "Test body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=TIMEOUT)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new_post["title"]

def test_api_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data