# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def fullName(self):
#         print("The persons name is:", self.name, self.surname)
#
# gerti = Person("Gerti", "Calaj")
# gerti.fullName()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2 * (self.length + self.width)

my_rect = Rectangle(7, 9)
area = my_rect.calc_area()
perimeter = my_rect.calc_perimeter()
print("Area:", area)
print("Perimeter:", perimeter)