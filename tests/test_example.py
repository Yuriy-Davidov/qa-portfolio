import requests

def test_tbank_site_is_available():
    response = requests.get('https://www.tbank.ru/')
    assert response.status_code == 200
    print("✅ Сайт Т-Банка работает!")
