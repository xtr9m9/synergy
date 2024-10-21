import random

class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [['.' for _ in range(self.width)] for _ in range(self.height)]  # Создаем пустое поле

    def display(self, helicopter):
        # Создаем копию поля для отображения вертолета
        display_field = [row.copy() for row in self.field]

        # Размещаем вертолет на поле
        display_field[helicopter.y][helicopter.x] = '🚁'  # Эмодзи для вертолета
        
        for row in display_field:
            print(' '.join(row))
        print("\n")

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def place_trees(self, num_trees):
        for _ in range(num_trees):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.field[y][x] = '🌳'  # Эмодзи для дерева

    def place_rivers(self, num_rivers):
        for _ in range(num_rivers):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.field[y][x] = '💧'  # Эмодзи для реки

    def ignite_trees(self, num_fires):
        for _ in range(num_fires):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.field[y][x] == '🌳':  # Если на клетке дерево
                self.field[y][x] = '🔥'  # Поджигаем его
        print("Некоторые деревья загорелись.")

    def spread_fire(self):
        new_fires = []
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] == '🔥':  # Если на клетке огонь
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Проверяем соседние клетки
                        nx, ny = x + dx, y + dy
                        if self.is_within_bounds(nx, ny) and self.field[ny][nx] == '🌳':
                            new_fires.append((nx, ny))  # Запоминаем, где новый огонь
        for nx, ny in new_fires:
            self.field[ny][nx] = '🔥'
        print("Пожар распространился.")

class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.water = 0  # Количество воды в резервуаре
        self.max_water = 1
        self.health = 3

    def move(self, direction, field):
        if direction == 'up' and field.is_within_bounds(self.x, self.y - 1):
            self.y -= 1
        elif direction == 'down' and field.is_within_bounds(self.x, self.y + 1):
            self.y += 1
        elif direction == 'left' and field.is_within_bounds(self.x - 1, self.y):
            self.x -= 1
        elif direction == 'right' and field.is_within_bounds(self.x + 1, self.y):
            self.x += 1
        print(f"Вертолет переместился в ({self.x}, {self.y})")

    def take_water(self, field):
        if field.field[self.y][self.x] == '💧':  # Если над рекой
            self.water = self.max_water
            print("Вертолет взял воду.")

    def extinguish_fire(self, field):
        if field.field[self.y][self.x] == '🔥' and self.water > 0:  # Если на пожаре
            field.field[self.y][self.x] = '.'  # Тушим пожар
            self.water -= 1
            print("Пожар потушен!")
        else:
            print("Здесь нет пожара или нет воды.")

# Создаем игровое поле размером 10x10
game_field = GameField(10, 10)
helicopter = Helicopter(0, 0)

game_field.place_trees(10)
game_field.place_rivers(5)
game_field.display(helicopter)

# Основной игровой цикл
while True:
    game_field.ignite_trees(1)  # Поджигаем деревья
    game_field.spread_fire()    # Пожар распространяется
    game_field.display(helicopter)

    command = input("Введите команду (up, down, left, right, take_water, extinguish): ")

    if command in ['up', 'down', 'left', 'right']:
        helicopter.move(command, game_field)
    elif command == 'take_water':
        helicopter.take_water(game_field)
    elif command == 'extinguish':
        helicopter.extinguish_fire(game_field)
