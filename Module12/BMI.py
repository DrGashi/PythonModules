from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.__weight = weight
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight < 0:
            ValueError("Weight cannot be negative")
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 0:
            ValueError("Height cannot be negative")
        self.__height = height

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m, "
              f"BMI: {self.calculate_bmi():2f}, Category: {self.get_bmi_category()}")

class Adult(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    def get_bmi_category(self):
        if self.calculate_bmi() < 18.5:
            return "Underweight"
        elif 18.5 <= self.calculate_bmi() < 24.9:
            return "Normal Weight"
        elif 24.9 <= self.calculate_bmi() < 29.9:
            return "Overweight"
        elif self.calculate_bmi() >= 29.9:
            return "Obese"

class Child(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)
    def calculate_bmi(self):
        return self.weight / (self.height ** 2) * 1.3
    def get_bmi_category(self):
        if self.calculate_bmi() < 14:
            return "Underweight"
        elif 14 <= self.calculate_bmi() < 18:
            return "Normal Weight"
        elif 18 <= self.calculate_bmi() < 24:
            return "Overweight"
        elif self.calculate_bmi() >= 24:
            return "Obese"

class BMIapp:
    def __init__(self):
        self.people = []
    def add_person(self, person):
        self.people.append(person)
    def collect_user_data(self):
        print("-----BMI Calculator---------")
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        if age >= 18:
            self.add_person(Adult(name, age, weight, height))
        else:
            self.add_person(Child(name, age, weight, height))
    def print_results(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            print()
            choice = input("Do you want to add another person(y/n): ")
            print()
            if choice != "y":
                break
        self.print_results()

bmi = BMIapp()
bmi.run()