import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5

def test_search_queries():
    with open("data/search_queries.txt", "r", encoding="utf-8") as f:
        queries = f.read().splitlines()

    for query in queries:
        response = requests.get(f"{BASE_URL}/posts?q={query}", timeout=TIMEOUT)
        assert response.status_code == 200
        print(f"✅ Запрос '{query}' прошёл успешно")