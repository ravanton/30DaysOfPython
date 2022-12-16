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
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
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
number_square = map(lambda x : x ** 2, numbers)
print(list(number_square))
# Use map to change each name to uppercase in the names list