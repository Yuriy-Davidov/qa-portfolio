def positive_sum(arr):
    total = 0
    for number in arr:
        if number > 0:
            total = total + number
    return total

# Проверяем работу функции
print(positive_sum([1, -4, 7, 12]))  # 20
print(positive_sum([-1, -2, -3]))    # 0
def positive_sum_short(arr):
    return sum(x for x in arr if x > 0)

# Проверяем короткую версию
print(positive_sum_short([1, -4, 7, 12]))  # 20
print(positive_sum_short([-1, -2, -3]))    # 0