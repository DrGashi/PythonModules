class Vehicle:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year
    def displayInfo(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make, model, year)
        self.body_style = body_style

class EV(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capacity = battery_capacity
    def charge(self):
        print("Charging EV")

rivian = EV("Rivian", "R1S", 2025, "SUV", 122.4)
rivian.displayInfo()
print("Body Style:", rivian.body_style)
print("Battery Capacity:", rivian.battery_capacity)
rivian.charge()