class Vehicle:
    def __init__(self, brand, model, year, mileage, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color


class PassengerCar(Vehicle):
    def __init__(self, brand, model, year, mileage, color, body_type, seats_count):
        super().__init__(brand, model, year, mileage, color)
        self.body_type = body_type
        self.seats_count = seats_count

    def info(self):
        print(f"{self.brand} {self.model} {self.year} {self.mileage} {self.color} {self.body_type} {self.seats_count}")

class FreightTruck(Vehicle):
    def __init__(self, brand, model, year, mileage, color, load_capacity_kg, trailer_attached):
        super().__init__(brand, model, year, mileage, color)
        self.load_capacity_kg = load_capacity_kg
        self.trailer_attached = trailer_attached

    def info(self):
        print(f"{self.brand} {self.model} {self.year} {self.mileage} {self.color} {self.load_capacity_kg} {self.trailer_attached}")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, mileage, color, battery_capacity_kwh, range_per_charge):
        super().__init__(brand, model, year, mileage, color)
        self.battery_capacity_kwh = battery_capacity_kwh
        self.range_per_charge = range_per_charge

    def info(self):
        print(f"{self.brand} {self.model} {self.year} {self.mileage} {self.color} {self.battery_capacity_kwh} {self.range_per_charge}")


car_1 = PassengerCar("Toyota", "Camry", 2020, 45000, "Чорний", "Седан", 5)
car_2 = PassengerCar("Volkswagen", "Tiguan", 2022, 12000, "Білий", "Кросовер", 5)

truck_1 = FreightTruck("Volvo", "FH16", 2018, 500000, "Синій", 20000, 3)
truck_2 = FreightTruck("MAN", "TGX", 2021, 150000, "Червоний", 18000, 2)

electro_1 = ElectricCar("Tesla", "Model 3", 2023, 5000, "Сірий", 75, 500)
electro_2 = ElectricCar("Nissan", "Leaf", 2019, 30000, "Зелений", 40, 270)

all_vehicles = [car_1, car_2, truck_1, truck_2, electro_1, electro_2]
for vehicle in all_vehicles:
    vehicle.info()