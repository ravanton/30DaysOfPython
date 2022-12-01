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

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def  add_all_nums(*nums):
    total = 0
    for num in nums:
         total += num
    return total
print("Total all numbers:", add_all_nums(2,3,45,65,3,254,65))
print(isinstance(add_all_nums, int)) 

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    
    F = (C * 9/5 ) + 32
    return F
print("Converts °C to °F:", convert_celsius_to_fahrenheit(C = 32))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):

    autumn = ("September", "October", "November")
    winter =("December", "January", "February")
    spring = ("March", "April", "May")
    summer =("June", "July", "August")

    

    if month in autumn:
        print("Autumn ")
    elif month in winter:
        print("Winter ")
    elif month in spring:
        print("Spring ")
    else:
        print("Summer ")
    return month
print(check_season(month="May"))
print(check_season("June"))
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(y1, y2, x1, x2):
    m = (y1 - y2) / (x1 - x2)
    return m
print("The slope of a linear equation:", calculate_slope(x1 = 2, x2 = 5, y1 = 5, y2 = 34))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn():
    pass
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    list = [1,2,3,4]
    return list
print(print_list(list))
