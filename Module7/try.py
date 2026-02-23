try:
    res = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

fruits = {
    "apple": 5,
    "banana": 7,
    "grape": 2
}
try:
    print(fruits["cherry"])
except KeyError:
    print("Key doesn't exist")