from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=r"yandexdriver.exe")

def test_tbank_open_page():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tbank.ru/")
    assert "Т-Банк" in driver.title
    driver.quit()

def test_tbank_search():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tbank.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)

    try:
        search_icon = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Поиск'], button[aria-label='Search']")
        driver.execute_script("arguments[0].click();", search_icon)
    except:
        search_icon = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Поиск']")
        driver.execute_script("arguments[0].click();", search_icon)

    time.sleep(1)

    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search'], input[placeholder='Поиск']"))
    )
    search_input.clear()
    search_input.send_keys("вклад")
    search_input.send_keys("\n")

    time.sleep(2)
    assert "вклад" in driver.page_source.lower()
    driver.quit()

def test_tbank_open_card():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tbank.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)

    buttons = driver.find_elements(By.TAG_NAME, "button")
    if len(buttons) > 0:
        driver.execute_script("arguments[0].click();", buttons[0])
        time.sleep(2)

    driver.quit()

def test_mobile_view():
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(390, 844)  # iPhone 12 размер
    driver.get("https://www.tbank.ru/")
    time.sleep(2)

    # Проверяем, что бургер-меню видно (иконка с тремя полосками)
    burger = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Меню']")
    assert burger.is_displayed()
    driver.quit()