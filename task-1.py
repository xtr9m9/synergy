# Задание 1: Подсчет нулей
N = int(input("Введите количество чисел: "))
count_zeros = 0

for _ in range(N):
    number = int(input())
    if number == 0:
        count_zeros += 1

print(f"Количество нулей: {count_zeros}")
