# syntax
# [i for i in iterable if expression]
language = "Python"
lst = [ i for i in language ]
print(type(lst))
print(lst)

# Generating numbers
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration
squares = [ i * i for i in range(11)]
print(squares)

# It is also possible to make a list of tuples
number = [(i, i * i ) for i in range(11)]
print(number)

# List comprehension can be combined with if expression
# Generating even numbers
even_number = [ i for i in range(21) if i % 2 == 0 ] # to generate even numbers in range 0 to 21
print(even_number)

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

# Creating a Lambda Function
# syntax
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))

add_two_number = lambda a, b : a + b 
print(add_two_number(5,9))

# Self invoking lambda function
print((lambda a, b: a + b)(2,3)) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(4))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
 
def power(x):
    return lambda n : x ** n

cube = power(2)(3) # function power now need 2 arguments to run, in separate rounded brackets
print(cube) # 8
two_power_of_live = power(2)(5)
print(two_power_of_live)

# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negative_and_zero  = [i for i in numbers if i <= 0 ]
print(only_negative_and_zero)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

one_dimensional_list = [ number for row in list_of_lists for number in row]
dimensional_list = [number for row in one_dimensional_list for number in row ]
print(dimensional_list)
# Using list comprehension create the following list of tuples:


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [''.join(inner) for inner in names] 

print(name_list)

# Change the following list of lists to a list of concatenated strings: