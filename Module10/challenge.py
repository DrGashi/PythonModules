class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses
    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self):
        return {
            "name": self.__name,
            "city": self.__city,
            "state": self.__state,
            "courses": self.__courses,
        }
    def organize_hackathon(self):
        pass

class Ds_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number
    @property
    def student_number(self):
        return self.__student_number
    @student_number.setter
    def student_number(self, student_number):
        self.__student_number = student_number
    def SCF(self):
        print(f"The Spring Code Fest will be held in may in {self.city}.")
    def organize_hackathon(self):
        print("The Hackathon will be held in Kino Armata, Prishtine")

class Ds_Prizren(DigitalSchool):
    def __init__(self, name, city, state, courses, address):
        super().__init__(name, city, state, courses)
        self.__address = address
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address

    def organize_hackathon(self):
        print("The Hackathon will be held in Prishtina so we have to travel by bus")
    def print_houses(self):
        print(f"{self.name} has the following houses: Hipsters, Engineers, Shadows and Speedsters")

ds_prsh = Ds_Prishtina("Digital School Prishtina", "Prishtina", "Kosovo", ["HTML & CSS", "Python", "PHP"], 10000)

ds_prsh.SCF()
ds_prsh.organize_hackathon()
print(f"The number of students in DS_Prishtina is {ds_prsh.student_number}")
print()

ds_prz = Ds_Prizren("Digital School Prizren", "Prizren", "Kosovo", "Web Development", "De Rada, M25, Prizren")
ds_prz.organize_hackathon()
ds_prz.print_houses()
print(f"The address of Digital School Prizren is {ds_prz.address}")
