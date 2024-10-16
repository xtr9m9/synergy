class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Класс Autobus наследует класс Transport
class Autobus(Transport):
    pass

# Создание объекта класса Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод результата
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")
