from select import error


def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "%":
        return number1 % number2
try:
    try:
        number1 = float(input("Enter the first number with decimal point: "))
        number2 = float(input("Enter the second number with decimal point: "))
        operator = input("Enter an arithmetic operator: ")
        try:
            print(calculate(number1, number2, operator))
        except:
            print("Cannot divide by zero!")
    except ValueError:
        print("You can only input numbers!")
except Exception:
    print("An error has ocurred!")
finally:
    print("No error has ocurred while trying to run this program")