# Если наша функция принимает параметры, мы должны вызывать ее с аргументами
  # syntax
  # Declaring a function
#   def function_name(para1, para2):
    # codes
    # codes
#   Calling function
#   print(function_name(arg1, arg2))
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Anton','Rud'))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + "N"
    return weight
print("Weight of an object in Newtons: ", weight_of_object(100, 9.81))

def greetings(name = "Anton "):
    fullname = name + " Whats up!"
    return fullname
print(greetings("Mark"))


# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_number(num1, num2):
    total = num1 + num2
    return total
print(add_two_number(10,2))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area
print("Area of  circule =", area_of_circle(2))

def  add_all_nums(*nums):
    total = 0
    for num in nums:
         total += num
    return total
print(type("Total all numbers:", add_all_nums(2,3,45,65,3,254,65)))
