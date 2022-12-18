# Функции высшего порядка
# В Python функции рассматриваются как объекты первого класса, что позволяет вам выполнять следующие операции над функциями:

# Функция может принимать одну или несколько функций в качестве параметров.
# Функция может быть возвращена как результат другой функции
# Функция может быть изменена
# Функция может быть назначена переменной

# Функция как параметр Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# Замыкания Python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Creating Decorators
## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

''' Python - Map Function
The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    map(function, iterable) '''

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

number_str = ['1', '2', '3', '4', '5']

number_int = map(int, number_str)
print(list(number_int))

# example
names = ['Garry', 'Ron', 'Hermione', 'Draco']  # iterable
names_upper_cased = map(lambda name : name.upper(), names)
print(list(names_upper_cased))



# Exercises: Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Italy']
names = ['Garry', 'Ron', 'Hermione', 'Draco']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use for loop to print each country in the countries list.
for country in countries:
    print(country)


# Use for to print each name in the names list.
for name in names:
    print(name)

# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# Use map to create a new list by changing each country to uppercase in the countries list
country_uppercase = map(lambda country: country.upper() , countries)
print(list(country_uppercase))

# Use map to create a new list by changing each number to its square in the numbers list
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))
# Use map to change each name to uppercase in the names list
names_uppercase =map(lambda name: name.upper(), names)
print(list(names_uppercase))

# Use filter to filter out countries containing 'land'.
def containing_land(country):
    if "land" in country:
        return True
    return False
land_country = filter(containing_land, countries)
print(list(land_country))

# Use filter to filter out countries having exactly six characters.
def exactly_six_characters(country):
    if len(country) == 6:
        return True
    return False
countries_six_characters = filter(exactly_six_characters, countries)
print(list(countries_six_characters))

# Use filter to filter out countries containing six letters and more in the country list.
def country_more_letter(country):
    if len(country) >= 6:
        return True
    return False
containing_more_letter = filter(country_more_letter, countries)
print(list(containing_more_letter))

# Use filter to filter out countries starting with an 'E'
def filter_country(country):
    if country.startswith("E"):
        return True
    return False

country_no_land = filter(filter_country,countries)
print(list(country_no_land))

print(*filter(lambda x: x[0] in 'I', countries))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_list(my_list):
    return list(filter(lambda x: isinstance(x, str), my_list))

print(get_string_list([1, 2, 3, "Garry", "Hermiona", 233]))

# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

total = reduce(lambda x, y: x + y, numbers) # returns 55
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatente_countries(x, y):
    return f"{x}, {y}"
all_countries = reduce(concatente_countries, countries)
print(f"{all_countries} are north European countries")

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# def categorize_countries(my_list):

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries):
    return countries[0:3]
print(get_first_ten_countries(countries))
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.