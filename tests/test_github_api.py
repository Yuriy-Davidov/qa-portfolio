import requests
import os

# Токен должен храниться в переменной окружения GITHUB_TOKEN
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = "Yuriy-Davidov"
BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_create_and_delete_repo():
    repo_name = "test-repo-qa"
    repo_data = {"name": repo_name, "auto_init": True}

    # 1. Создаём репозиторий
    response = requests.post(f"{BASE_URL}/user/repos", json=repo_data, headers=headers)
    assert response.status_code == 201, "Репозиторий не создался"
    print(f"✅ Репозиторий '{repo_name}' создан")

    # 2. Проверяем, что он появился в списке
    response = requests.get(f"{BASE_URL}/user/repos", headers=headers)
    assert response.status_code == 200
    repos = [repo["name"] for repo in response.json()]
    assert repo_name in repos, "Репозиторий не найден в списке"
    print("✅ Репозиторий найден в списке")

    # 3. Удаляем репозиторий
    response = requests.delete(f"{BASE_URL}/repos/{GITHUB_USER}/{repo_name}", headers=headers)
    assert response.status_code == 204, "Не удалось удалить репозиторий"
    print("✅ Репозиторий удалён")