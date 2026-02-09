print()
class Personi:
    def __init__(self, emri):
        self.emri = emri

    def fol(self, mesejxh):
        print(f"{self.emri} thotë '{mesejxh}'")

    def getEmri(self):
        return self.emri

gerti = Personi("Gerti")
amanti = Personi("Amanti")
deoni = Personi("Deoni")

gerti.fol("Unë jam ma i miri")
amanti.fol("Unë jam tu i ngjeh centat")
deoni.fol("Po më hahet ni hamburger")

print("Emri i nxenesit te pare", gerti.getEmri())
print("Emri i nxenesit te dyte", amanti.getEmri())
print("Emri i nxenesit te trete", deoni.getEmri())

print()

def greetPerson(name):
    print("Hello", name)
greetPerson("Dren")