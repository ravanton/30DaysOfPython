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
even_number = [ i for i in range(21) if i % 2 == 0 ]
print(even_number)
