import openai
import pytest
import os
import sys

# ⚠️ ВСТАВЬ СВОЙ API-КЛЮЧ СЮДА (для проверки)
openai.api_key = "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"

def analyze_error(error_message):
    try:
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты — QA-эксперт. Анализируй ошибки тестов и предлагай возможные причины."},
                {"role": "user", "content": f"Ошибка теста: {error_message}\n\nКакая возможная причина и как исправить?"}
            ],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при вызове OpenAI API: {str(e)}"

def test_ai_analysis():
    try:
        assert 1 == 2, "Намеренная ошибка"
    except AssertionError as e:
        error_text = str(e)
        sys.stdout.write("\n🔍 AI-анализ ошибки:\n")
        analysis = analyze_error(error_text)
        sys.stdout.write(analysis + "\n")
        pytest.skip("Тест упал, но AI-анализ выполнен")