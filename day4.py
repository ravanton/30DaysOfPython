# Интерполяция строк
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

# Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity")
print("\nAnton\t250\tUSA\t\'Miami\'")

# Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash = "# ".join(list)
print(hash)

str = "Coding For All".capitalize().title()

print(str.replace("Coding", "Python3"))
print(str.startswith("Coding"))
print(str.replace("Coding", ""))