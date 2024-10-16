class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    # Метод для движения вверх
    def go_up(self):
        self.y += self.s
        print(f"Черепашка переместилась вверх. Текущая позиция: ({self.x}, {self.y})")

    # Метод для движения вниз
    def go_down(self):
        self.y -= self.s
        print(f"Черепашка переместилась вниз. Текущая позиция: ({self.x}, {self.y})")

    # Метод для движения влево
    def go_left(self):
        self.x -= self.s
        print(f"Черепашка переместилась влево. Текущая позиция: ({self.x}, {self.y})")

    # Метод для движения вправо
    def go_right(self):
        self.x += self.s
        print(f"Черепашка переместилась вправо. Текущая позиция: ({self.x}, {self.y})")

    # Метод для увеличения шага
    def evolve(self):
        self.s += 1
        print(f"Шаг увеличен. Текущий шаг: {self.s}")

    # Метод для уменьшения шага
    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print(f"Шаг уменьшен. Текущий шаг: {self.s}")
        else:
            raise ValueError("Шаг не может быть меньше или равен нулю!")

    # Метод для подсчета минимального количества перемещений
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves = (dx + dy) // self.s
        print(f"Минимальное количество перемещений до ({x2}, {y2}): {moves}")
        return moves


turtle = Turtle(0, 0, 2)
turtle.go_up()
turtle.go_right()
turtle.evolve()
turtle.count_moves(10, 10)
turtle.degrade()
