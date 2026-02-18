class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"
    def get_private_variable(self):
        return self.__private_variable
    def __private_method(self):
        print("This is a private method")
my_class = MyClass()
print(my_class.get_private_variable())
