# Задание 2: Подсчет делителей числа
X = int(input("Введите натуральное число: "))
divisors_count = 0

for i in range(1, int(X**0.5) + 1):
    if X % i == 0:
        divisors_count += 1
        if i != X // i:
            divisors_count += 1

print(f"Количество делителей числа {X}: {divisors_count}")
