## 1. Требования
- Python 3.10 или выше
- Git (опционально)
- 
## 2. Клонирование репозитория

git clone https://github.com/Yuriy-Davidov/qa-portfolio.git
cd qa-portfolio

## 3. Создание виртуального окружения
Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

## 4. Установка зависимостей

pip install -r requirements.txt

## 5. Запуск тестов

python -m pytest tests/test_example.py -v

## 6. Ожидаемый результат
Все тесты должны завершиться с результатом **PASSED**.
