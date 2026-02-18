class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
dreni = Person("Dren", 16)
gerti = Person("Gerti", 12)
amant = Person("Amant", 13)
dreni.greet()
gerti.greet()
amant.greet()