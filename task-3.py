# Задание №1

# Ввод данных
N = int(input())  # Читаем число N
numbers = [int(input()) for _ in range(N)]  # Вводим массив чисел

# Переворачиваем массив
numbers.reverse()

# Выводим результат
print(*numbers)

# Задание №2

# Ввод данных
N = int(input())  # Читаем число N
numbers = list(map(int, input().split()))  # Читаем массив чисел

# Переставляем элементы
result = []
for i in range(N//2):
    result.append(numbers[N-1-i])
    result.append(numbers[i])
if N % 2 == 1:
    result.append(numbers[N//2])

# Выводим результат
print(*result)

# Задание №3

# Ввод данных
m = int(input())  # Максимальная масса лодки
n = int(input())  # Количество рыбаков
weights = [int(input()) for _ in range(n)]  # Вес рыбаков

# Сортируем веса рыбаков
weights.sort()

# Количество лодок
boats = 0
left = 0
right = n - 1

while left <= right:
    if weights[left] + weights[right] <= m:  # Если двоих можно перевезти
        left += 1  # Отправляем самого лёгкого
    right -= 1  # Отправляем самого тяжёлого
    boats += 1  # Каждое действие — новая лодка

# Выводим результат
print(boats)
