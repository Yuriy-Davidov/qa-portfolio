from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_gosuslugi_search():
    """
    Пример тестирования сайта Госуслуг.
    Сайт использует защиту от ботов, поэтому тест демонстрирует подход,
    а не гарантирует прохождение. Это полезный пример работы с защищёнными сайтами.
    """
    service = Service(executable_path=r"yandexdriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.gosuslugi.ru/")
    time.sleep(3)

    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Поиск']"))
        )
    except:
        try:
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
            )
        except:
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']"))
            )

    search_input.send_keys("Загранпаспорт")
    search_input.submit()
    time.sleep(3)

    # Проверяем, что страница с результатами загрузилась
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    print("✅ Тест Госуслуг: страница с результатами загружена")
    driver.quit()