"""
Автотест, который читает данные из файла и проверяет их
"""

import requests

def test_search_queries():
    """
    Проверяет, что поисковые запросы из файла работают
    (учебный пример, проверяет только доступность сайта)
    """
    # Читаем запросы из файла
    with open("data/search_queries.txt", "r", encoding="utf-8") as f:
        queries = f.read().splitlines()
    
    base_url = "https://www.tbank.ru/"
    
    for query in queries:
        # Формируем URL для поиска (учебный пример)
        search_url = f"{base_url}?search={query}"
        response = requests.get(search_url)
        
        # Проверяем, что сайт отвечает
        assert response.status_code == 200, f"Ошибка для запроса: {query}"
        print(f"✅ Запрос '{query}' прошёл успешно")