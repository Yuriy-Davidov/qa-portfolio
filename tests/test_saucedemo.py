from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"yandexdriver.exe")

def test_saucedemo_login():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    # Явно ждём, пока поле станет кликабельным
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password.send_keys("secret_sauce")

    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_btn.click()

    # Проверяем, что попали на главную страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Добавляем первый товар в корзину
    add_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )
    add_btn.click()

    # Проверяем, что в корзине появился 1 товар
    cart_badge = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"

    driver.quit()