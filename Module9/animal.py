class Animal:
    def sound(self):
        print("Animals make noise")
    def sounds(self):
        return "noise"
class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")
    def sounds(self):
        return "Woof Woof"
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")
    def sounds(self):
        return "Meow Meow"
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()

print(f"The dog goes {dog.sounds()} and the cat goes {cat.sounds()}")