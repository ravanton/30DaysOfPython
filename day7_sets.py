# Creating a Set
# We use curly brackets, {} to create a set or the set() built-in function.

# Creating an empty set
# syntax
st = {}
# or
st = set()
# Creating a set with initial items
# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# Exercises Day 7 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Pandadoc', 'Ubisoft', 'Rockstar'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Ubisoft')
print(it_companies)
# What is the difference between remove and discard
"""Если элемент не найден , метод remove() вызовет ошибки, поэтому полезно проверить, существует ли элемент в заданном наборе. Однако метод discard() не вызывает никаких ошибок. """
