import random

# Функция для генерации матрицы размером n x m
def generate_matrix(rows, cols):
    return [[random.randint(-200, 200) for _ in range(cols)] for _ in range(rows)]

# Функция для сложения двух матриц
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Размер матриц
rows, cols = 10, 10

# Генерация двух матриц
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

# Сложение матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

# Вывод результатов
print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (Result of addition):")
for row in matrix_3:
    print(row)
