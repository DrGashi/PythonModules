class Person:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def calculate_bmi(self):
        pass
    def get_bmi_category(self):
        pass
    def print_info(self):
        pass

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height

class Adult(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)
    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 1)
    def get_bmi_category(self):
        if self.calculate_bmi() < 18.5:
            return "Underweight"
        elif 18.5 <= self.calculate_bmi() < 24.9:
            return "Normal Weight"
        elif 24.9 <= self.calculate_bmi() < 29.9:
            return "Overweight"
        elif self.calculate_bmi() >= 29.9:
            return "Obese"
        else:
            return "Please input a valid height and weight"
    def print_info(self):
        print(f"{self.name}'s BMI is : {self.calculate_bmi()}({self.get_bmi_category()})")

class Child(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)
    def calculate_bmi(self):
        return round((self.weight / (self.height ** 2)) * 1.3,1)
    def get_bmi_category(self):
        if self.calculate_bmi() < 14:
            return "Underweight"
        elif 14 <= self.calculate_bmi() < 18:
            return "Normal Weight"
        elif 18 <= self.calculate_bmi() < 24:
            return "Overweight"
        elif self.calculate_bmi() >= 24:
            return "Obese"
        else:
            return "Please input a valid height and weight"
    def print_info(self):
        print(f"{self.name}'s BMI is : {self.calculate_bmi()}({self.get_bmi_category()})")
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
        if age < 10:
            self.add_person(Child(name, age, weight, height))
        else:
            self.add_person(Adult(name, age, weight, height))
    def print_results(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            print()
            choice = input("Do you wish to continue(y/n): ")
            print()
            if choice != "y":
                print()
                self.print_results()
                break

bmi = BMIapp()
bmi.run()