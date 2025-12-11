"""
Клас описання автомобіля
"""

class Car:
    car_list = []
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        Car.car_list.append(self)

    def __str__(self):
        return f"Автомобіль: {self.make} {self.model} {self.year}"

    class CarShowroom:
        def __init__(self, car_list):
            self.car_list = car_list

        def car_sales(self):
            user_choise = input("Введіть марку або модель бажаного автомобіля зі списку: ").strip()
            found = False
            for c in self.car_list:
                if user_choise == c.make or user_choise == c.model:
                    found = True
                    print(f"Ціна автомобіля: {c.price}")
                    while True:
                        result = input("Купити? (y або n): ")
                        if result == "y":
                            print(f"Вітаю, ви купили: {c.make} {c.model}")
                            break
                        elif result == "n":
                            print("Дуже шкода! Будемо очікувати вашого рішення!")
                            break
                        else:
                            print("Невірний ввод!")
                    break
            if not found:
                print("На жаль, такого автомобіля немає у продажу.")


car_1 = Car("Toyota", "Camry", 2022, 27000)
car_2 = Car("BMW", "X5", 2023, 65000)
car_3 = Car("Tesla", "Model 3", 2024, 42000)
car_4 = Car("Hyundai", "Solaris", 2019, 12000)
car_5 = Car("Porsche", "911 Carrera", 2021, 115000)

print("В наявності:")
for car in Car.car_list:
    print(car)
cars_sales = Car.CarShowroom(Car.car_list)
cars_sales.car_sales()

