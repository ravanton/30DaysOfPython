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
def print_list(list_param):
    result = []
    for x in list_param:
        result.append(x)
    
    return result
print(print_list([56,76,87]))

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(hi_list):
    reverse_list = []
    
    for h in reversed(hi_list): # add Elements in Reversed Order
        reverse_list.append(h)
    
    return reverse_list
print(reverse_list(["V","C","R"]))
print(reverse_list([1, 2, 3, 4, 5]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(my_list):
    new_list = []
    
    for h in my_list:
        new_list.append(h.capitalize())
    
    return new_list
print(capitalize_list_items(['anton', 'developer']))

# Объявите функцию с именем add_item. Он принимает список и параметры элемента. Он возвращает список с элементом, добавленным в конце.
def add_item(list):

    my_list = ['banana', 'orange', 'mango', 'lemon']

    for s in list:
        my_list.append(s)
    return my_list


print(add_item(['kiwi']))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(remove):

    fruits = ["apple", "mango", "watermelow"]

    for f in remove:
        fruits.remove(f)
    return fruits

print(remove_item( ["apple"]))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    
    total =  sum(range(number + 1))
        
        
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(numbers):
    total = 0 
    for n in range(numbers + 1):
        if n % 2 != 0:
            total += n
    return total
print(sum_of_odds(4))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(numbers):
    total = 0
    for number in range(numbers + 1):
        if number % 2 == 0:
            total += number
    return total
print(sum_of_even(4))