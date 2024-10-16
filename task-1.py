class CashRegister:
    def __init__(self, balance=0):
        self.balance = balance

    # Метод для пополнения кассы
    def top_up(self, amount):
        self.balance += amount
        print(f"Касса пополнена на {amount}. Текущий баланс: {self.balance}")

    # Метод для подсчета количества целых тысяч
    def count_1000(self):
        thousands = self.balance // 1000
        print(f"В кассе {thousands} целых тысяч.")
        return thousands

    # Метод для снятия денег с кассы
    def take_away(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе!")
        self.balance -= amount
        print(f"Из кассы забрано {amount}. Текущий баланс: {self.balance}")
