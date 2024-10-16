class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Класс Autobus с переопределением метода seating_capacity
class Autobus(Transport):
    def seating_capacity(self, capacity=50):  # Устанавливаем значение по умолчанию 50
        return super().seating_capacity(capacity)

# Создание объекта класса Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод результата
print(bus.seating_capacity())  # Значение по умолчанию - 50
