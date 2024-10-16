# Задание 3: Вывод четных чисел на отрезке
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

even_numbers = [str(i) for i in range(A, B + 1) if i % 2 == 0]
print(" ".join(even_numbers))
