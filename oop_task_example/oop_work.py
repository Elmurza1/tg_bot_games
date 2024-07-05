class Car:
    def __init__(self, mark_pm, model_pm, year_pm, price_pm ):
        self.mark = mark_pm
        self.model = model_pm
        self.year = year_pm
        self.price = price_pm

    def info(self):
        print(f'марка {self.mark}, год {self.year}, цена {self.price}, модель {self.model}')



car1 = Car('tesla', 'x', 2024, 40000)
car2 = Car('bmw', 'm8', 2020, 150000)
car3 = Car('maclaren', 'P1', 2023, 600000)

car1.info()
car3.info()
car2.info()

print(car2.price + car3.price + car1.price)