def add(x, y):
    return x + y
def operate(operation, x, y):
    return operation(x, y)

result = operate(add, 5, 7)
print(result)