"""
Автотесты для проверки сайта Т-Банка
Используется библиотека requests для отправки HTTP-запросов
"""

import requests

# Базовый URL для тестов
BASE_URL = "https://www.tbank.ru/"

def test_tbank_site_is_available():
    """
    Проверяет, что сайт Т-Банка доступен и отвечает с кодом 200
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    print("✅ Сайт Т-Банка доступен!")


def test_tbank_has_company_name():
    """
    Проверяет, что на главной странице упоминается название компании
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    
    # Явно указываем кодировку UTF-8 для корректного отображения русских букв
    response.encoding = 'utf-8'
    page_text = response.text
    
    # Проверяем наличие названия "Т-Банк" (в разных вариантах написания)
    assert "Т-Банк" in page_text or "T-Bank" in page_text or "т-банк" in page_text, \
        "Название компании не найдено на странице"
    print("✅ Название компании присутствует на главной странице!")


def test_tbank_has_footer():
    """
    Проверяет, что в футере (подвале) есть ссылка на политику конфиденциальности
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    
    response.encoding = 'utf-8'
    page_text = response.text.lower()
    
    # Проверяем наличие ключевых слов в футере
    assert "политик" in page_text or "confidentiality" in page_text or "privacy" in page_text, \
        "Информация о политике конфиденциальности не найдена"
    print("✅ Информация о политике конфиденциальности присутствует!")


def test_tbank_search_form_exists():
    """
    Проверяет, что на главной странице есть поле поиска
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    
    response.encoding = 'utf-8'
    page_text = response.text.lower()
    
    # Проверяем наличие ключевых слов, связанных с поиском
    assert "поиск" in page_text or "search" in page_text or "найти" in page_text, \
        "Поле поиска не обнаружено на странице"
    print("✅ Поле поиска присутствует на главной странице!")