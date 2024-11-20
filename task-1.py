# Задание №1

# Ввод данных
N = int(input())  # Количество чисел
numbers = list(map(int, input().split()))  # Список чисел

# Находим количество уникальных чисел
unique_numbers = len(set(numbers))

# Выводим результат
print(unique_numbers)

# Задание №2

# Ввод данных для двух списков
list1_size = int(input())  # Размер первого списка
list1 = set(map(int, input().split()))  # Первый список (множество для быстрого поиска)

list2_size = int(input())  # Размер второго списка
list2 = set(map(int, input().split()))  # Второй список (множество для быстрого поиска)

# Находим пересечение двух множеств
common_elements = list1.intersection(list2)

# Выводим результат
print(len(common_elements))

# Задание №3

# Ввод данных
numbers = list(map(int, input().split()))  # Последовательность чисел

# Множество для отслеживания уже встреченных чисел
seen = set()

# Проверка каждого числа
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
