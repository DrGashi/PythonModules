sentence = "Hello, world"
for char in sentence:
    if not char.isalpha():
        print(char)

for x in range(1,6):
    print("Numri", x)

numbers = [12, 87, 45, 82, 34, 69, 34, 76, 12, 65, 34, 75, 23, 54]
max_value = numbers[0]
for number in numbers:
    if max_value < number:
        max_value = number
print(max_value)

