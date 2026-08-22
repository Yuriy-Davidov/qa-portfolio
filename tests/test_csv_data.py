import csv
import requests

def test_csv_data_validation():
    with open("data/users.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 3, "Должно быть 3 строки"
    for row in rows:
        assert "@" in row["email"], f"Неверный email: {row['email']}"
        assert int(row["age"]) > 0, f"Возраст должен быть > 0: {row['age']}"
        print(f"✅ {row['name']} ({row['email']}) — OK")

def test_send_data_to_api():
    with open("data/users.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        response = requests.post(
            "https://jsonplaceholder.typicode.com/users",
            json=row,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 201
        print(f"✅ Данные для {row['name']} отправлены")
