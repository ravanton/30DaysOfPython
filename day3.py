print(3 > 2) # True, because 3 is greater than 2
print(3 >= 2)
print(3 == 2) # False, because 3 is not equal to 2
print(3 != 2) # True, because 3 is not equal to 2

print(len('python') > len('dragon')) # False


# Comparing something gives either a True or False # Сравнение чего-либо дает либо истинное, либо ложное значение
print('True == True: ', True == True)
print("False == True:", True == False)

print('True or False:', True or False)

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false

print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False

#💻 Exercises - Day 3
age = int(22)
print(age)
my_height = float(183.4)
print(my_height)
number_complex = complex(1 + 2j)
print(number_complex)

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter Base: "))
height = int(input("Enter height: "))
area = height * base * 0.5
print("The area of the triangle is", area)