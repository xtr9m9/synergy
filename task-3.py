# Задание 3: Инвесторы
X = int(input("Минимальная сумма инвестиций: "))
A = int(input("У Майкла есть: "))
B = int(input("У Ивана есть: "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)
