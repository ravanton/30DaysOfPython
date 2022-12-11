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