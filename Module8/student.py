class Student:
    school_name = "Digital School"
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. I am in {self.school_name}, in the {self.course} course."

dreni = Student("Dren", 16, "Python Advanced")
print(dreni.greet())