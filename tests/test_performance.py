import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5

def test_api_performance():
    times = []
    for i in range(50):
        start = time.time()
        response = requests.get(f"{BASE_URL}/posts/{i+1}", timeout=TIMEOUT)
        end = time.time()
        times.append(end - start)
        assert response.status_code == 200

    avg_time = sum(times) / len(times)
    assert avg_time < 1.0, f"Среднее время ответа {avg_time:.2f} сек > 1.0 сек"
    print(f"✅ Среднее время ответа: {avg_time:.2f} сек")