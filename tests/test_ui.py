from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_tbank_ui():
    service = Service(executable_path=r"yandexdriver.exe") # путь к скачанному файлу
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tbank.ru/")
    assert "Т-Банк" in driver.title
    driver.quit()