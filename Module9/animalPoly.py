from Functions.JavaPrint import SystemOutPrintln

class Dog():
    def __init__(self, name):
        self.name = name
    def sound(self):
        SystemOutPrintln(f"{self.name} makes the sound Woof!")

class Cat():
    def __init__(self, name):
        self.name = name
    def sound(self):
        SystemOutPrintln(f"{self.name} makes the sound Mewo!")

class Bird():
    def __init__(self, name):
        self.name = name
    def sound(self):
        SystemOutPrintln(f"{self.name} makes the sound Chirp!")

dog = Dog("Max Verstappen")
cat = Cat("Otto Von Bismarck")
bird = Bird("Nelson Mandela")

for animal in(dog, cat, bird):
    animal.sound()