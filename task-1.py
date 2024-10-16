# Последовательность
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Рекурсивная функция для вывода элементов списка
def print_list_recursively(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_list_recursively(lst, index + 1)  # Рекурсивный вызов с увеличением индекса
    else:
        print("Конец списка")

# Вызов функции
print_list_recursively(my_list)
