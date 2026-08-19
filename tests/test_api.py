"""
Автотесты для проверки API (учебный пример)
Используется публичное API для демонстрации навыков
"""

import requests

# Используем публичное API для тестов (JSONPlaceholder)
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_get_posts():
    """
    Проверяет, что API возвращает список постов (GET-запрос)
    """
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    print("✅ API /posts вернул список постов")


def test_api_create_post():
    """
    Проверяет, что можно создать новый пост (POST-запрос)
    """
    new_post = {
        "title": "QA Portfolio Test",
        "body": "This is a test post from my portfolio",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    print("✅ API /posts создал новый пост")


def test_api_get_post_by_id():
    """
    Проверяет, что можно получить конкретный пост по ID
    """
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data
    print(f"✅ Пост с ID {post_id} успешно получен")