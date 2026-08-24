import requests
from bs4 import BeautifulSoup

def test_gosuslugi_smoke():
    """
    Smoke-тест для проверки доступности и базовых элементов
    главной страницы портала «Госуслуги».
    """
    url = "https://www.gosuslugi.ru/"
    
    # 1. Проверка доступности сайта
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    print(f"✅ Статус-код: {response.status_code}")
    
    # 2. Проверка заголовка страницы
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else ""
    expected_title = "Госуслуги"
    assert expected_title in title, f"В заголовке '{title}' нет '{expected_title}'"
    print(f"✅ Заголовок: '{title}'")
    
    # 3. Проверка наличия ключевого элемента (ссылка "Войти")
    login_link = soup.find("a", string="Войти") or soup.find("a", string="Личный кабинет")
    assert login_link is not None, "Ссылка 'Войти' не найдена на главной странице"
    print("✅ Ссылка 'Войти' найдена")
    
    print("\n🎉 Все проверки smoke-теста пройдены успешно!")

if __name__ == "__main__":
    test_gosuslugi_smoke()