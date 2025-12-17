class Car:
    def __init__(self, brand, model, year, color, fuel_max, speed_max, consumption_100km):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_max = fuel_max
        self.speed_max = speed_max
        self.consumption_100km = consumption_100km
        self.__fuel = 0
        self.__speed = 0
        self.__engine_on = False

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.year} року, колір: {self.color}, об'єм баку: {self.fuel_max}л"

    @property
    def fuel(self):
        return self.__fuel

    def refuel(self, count):
        if count < 0:
            print("Неможлива дія")
        else:
            self.__fuel += count
            if self.__fuel > self.fuel_max:
                quantity = self.__fuel - self.fuel_max
                self.__fuel = self.fuel_max
                print(f"Ви заправили автомобіль на {count - quantity}  до повного баку")

    @property
    def speed(self):
        return self.__speed

    def drive(self, distance, car_speed):
        if car_speed > self.speed_max:
            print("Ця швидкість вище максимальної швидкості автомобіля")
            return
        if self.engine_on and self.__fuel > 0:
            self.__speed = car_speed
            cost = distance * self.consumption_100km / 100
            if cost > self.__fuel:
                print(f"Бінзин закінчився! Ви проїхали {self.__fuel * 100 / self.consumption_100km}")
                self.stop_engine()
                return
            self.__fuel -= cost
            print(f"Після відстані {distance} залишилось {self.__fuel} бінзину")
            time = distance * 60 / self.__speed
            print(f"Відстань {distance} пройдена за {time} хвилин")
        else:
            print("Рух автомобіля неможливий")

    def stop(self):
        self.__speed = 0
        print("Автомобіль зупинено")


    @property
    def engine_on(self):
        return self.__engine_on

    def start_engine(self):
        if self.__fuel > 0:
            self.__engine_on = True
            print(f"Двигун працює. Автомобіль {self.brand}, {self.model} почав рух")
        else:
            print("Недостатньо топлива")

    def stop_engine(self):
        if self.__speed > 0:
            print("Зупиніться, щоб заглушити двигун!!")
        else:
            self.__engine_on = False
            print("Двигун виключен")

car_1 = Car("Toyota", "AURIS", 2009, "червона", 50, 150, 10)
print(car_1)
car_1.refuel(60)
car_1.drive(60, 50)
car_1.start_engine()
car_1.drive(60, 50)
car_1.stop()
car_1.stop_engine()