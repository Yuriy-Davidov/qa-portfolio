# QA Portfolio — (осень 2026)

## Обо мне
Начинающий QA-инженер.  
Изучаю Python, автоматизацию тестирования и основы тест-дизайна.

## Навыки
- Python (базовый), pytest, requests
- Git, GitHub
- Понимание HTTP, клиент-серверного взаимодействия
- Составление тест-кейсов и баг-репортов

## 📂 Структура проекта

### Автотесты (`tests/`)
| Файл | Что проверяет |
|------|---------------|
| [`test_example.py`](tests/test_example.py) | Доступность сайта Т-Банка, наличие названия компании |
| [`test_api.py`](tests/test_api.py) | Работу публичного API (GET, POST, получение по ID) |
| [`test_with_data.py`](tests/test_with_data.py) | Поисковые запросы из файла `data/search_queries.txt` |
| [`test_ui.py`](tests/test_ui.py) | UI-тесты через Selenium (открытие страницы, поиск, клик по кнопке) |
| [`test_performance.py`](tests/test_performance.py) | Нагрузочное тестирование API (50 запросов, проверка скорости ответа) |
| [`test_ui.py` (mobile)](tests/test_ui.py) | Мобильная версия сайта (iPhone 12, проверка бургер-меню) |
| [`test_with_ai.py`](tests/test_with_ai.py) | AI-анализ ошибок через OpenAI API (ChatGPT) |
| [`test_saucedemo.py`](tests/test_saucedemo.py) | Тестирование логина и добавления в корзину на Saucedemo |
| [`test_github_api.py`](tests/test_github_api.py) | GitHub API: создание, проверка и удаление репозитория через токен |
| [`test_csv_data.py`](tests/test_csv_data.py) | Чтение CSV, валидация данных, отправка в API |
| [`test_smoke_gosuslugi.py`](tests/test_smoke_gosuslugi.py) | Smoke-тест главной страницы портала «Госуслуги» (проверка доступности, заголовка, ключевых элементов) |
| [`test_gosuslugi_search.py`](tests/test_gosuslugi_search.py) | Пример тестирования защищённого сайта (Госуслуги), демонстрация подхода к поиску элементов |


### Баг-репорты (`bugs/`)
- `bug-report-template.md` — шаблон для оформления багов
- `bug-001-training.md` — учебный баг-репорт №1
- `bug-002-training.md` — учебный баг-репорт №2

### Тест-кейсы (`testcases/`)
- `test-cases-template.md` — 5 готовых тест-кейсов для формы регистрации

### Данные для тестов (`data/`)
- `search_queries.txt` — список поисковых запросов для Data-Driven теста

### Скриншоты (`screenshots/`)
- [Результат запуска всех тестов](screenshots/tests-passed.png)
- [Результат нагрузочного теста](screenshots/performance-test-passed.png)
- [Результат мобильного теста (ошибка)](screenshots/mobile-test-failed.png)
- [AI-анализ ошибки (регион заблокирован)](screenshots/ai-test-error.png)
- [Результат теста Saucedemo](screenshots/saucedemo-test-passed.png)
- [GitHub API тест](screenshots/github-api-test-passed.png)
- [CSV-тест](screenshots/csv-test-passed.png)

## 🚀 Как запустить тесты
```bash
pytest
```

## 🧰 Дополнительные артефакты

### SQL-запросы
- [Примеры запросов](sql/queries.sql)
- Выборка, объединение таблиц, группировка

### Postman-коллекция
- [API-тесты (reqres.in)](postman/collection.json)
- Запуск через Newman: `newman run postman/collection.json`

## Контакты
- GitHub: [Yuriy-Davidov](https://github.com/Yuriy-Davidov)

---

## English version

# QA Portfolio — (Autumn 2026)

## About Me
Junior QA Engineer.  
Learning Python, test automation, and test design fundamentals.

## Skills
- Python (basic), pytest, requests, selenium
- Git, GitHub
- Understanding of HTTP, client-server architecture
- Writing test cases and bug reports

---

## 📂 Project Structure

### Automated Tests (`tests/`)
| File | Description |
|------|-------------|
| `test_example.py` | T-Bank site availability, company name check |
| `test_api.py` | Public API tests (GET, POST, fetch by ID) |
| `test_with_data.py` | Data-Driven tests from `data/search_queries.txt` |
| `test_ui.py` | UI tests via Selenium (page open, search, button click) |
| `test_performance.py` | API performance testing (50 requests, response time check) |
| `test_ui.py` (mobile) | Mobile version testing (iPhone 12, burger menu check) |
| `test_with_ai.py` | AI error analysis via OpenAI API (ChatGPT) |
| `test_saucedemo.py` | Saucedemo login and add to cart test |
| `test_github_api.py` | GitHub API: create, check and delete repo using token |
| `test_csv_data.py` | CSV reading, data validation and sending to API |

### Bug Reports (`bugs/`)
- `bug-report-template.md` — bug report template
- `bug-001-training.md` — sample bug report #1
- `bug-002-training.md` — sample bug report #2

### Test Cases (`testcases/`)
- `test-cases-template.md` — 5 test cases for registration form

### Test Data (`data/`)
- `search_queries.txt` — search queries for Data-Driven tests

### Screenshots (`screenshots/`)
- [All tests passed](screenshots/tests-passed.png)
- [Performance test passed](screenshots/performance-test-passed.png)
- [Mobile test (failed)](screenshots/mobile-test-failed.png)
- [AI error analysis (region blocked)](screenshots/ai-test-error.png)
- [Saucedemo test passed](screenshots/saucedemo-test-passed.png)
- [GitHub API test](screenshots/github-api-test-passed.png)
- [CSV test](screenshots/csv-test-passed.png)

---

## 🚀 How to Run Tests
```bash
pytest
```
## 🧰 Additional Artifacts

### SQL Queries
- [Query examples](sql/queries.sql)
- SELECT, JOIN, GROUP BY

### Postman Collection
- [API tests (reqres.in)](postman/collection.json)
- Run via Newman: `newman run postman/collection.json`

---

## Contacts
- GitHub: [Yuriy-Davidov](https://github.com/Yuriy-Davidov)
