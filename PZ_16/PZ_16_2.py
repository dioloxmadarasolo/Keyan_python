class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model}, {self.year} г.в."

class Car(Transport):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def car_info(self):
        base_info = super().info()
        print(f"{base_info}, тип кузова: {self.body_type}")

my_car = Car("Toyota", "Camry", 2020, "седан")
my_car.car_info()