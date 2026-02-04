count = 1
while count <= 10:
    print("Number", count)
    count += 1
print()

while True:
    user_input = input("Enter a positive number: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break
    print("Invalid input. Please try again")
print("You entered a valid poitive number: ", number)

print()

names = ["Dren Gashi", "Gerti Calaj", "Deon Beka", "Amant Zabeli"]
for name in names:
    print(name)