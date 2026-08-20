# Инструкция по установке и запуску тестов

## 1. Требования
- Python 3.10 или выше
- Git (опционально)

---

## 2. Клонирование репозитория
```bash
git clone https://github.com/Yuriy-Davidov/qa-portfolio.git
cd qa-portfolio
```

---

## 3. Создание виртуального окружения

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

---

## 5. Запуск тестов
```bash
python -m pytest tests/test_example.py -v
```

---

## 6. Ожидаемый результат
Все тесты должны завершиться с результатом **PASSED**.
