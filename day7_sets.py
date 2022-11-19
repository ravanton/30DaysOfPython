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

# Exercises: Level 2
# Join A and B
C = A.union(B)
print(C)
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print("Is A subset of B: ", A.issubset(B))
# Are A and B disjoint sets
print("Are A and B disjoint sets: ", A.isdisjoint(B))
# Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)
print(A_with_B)
print(B_with_A)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# {27,28}
# Delete the sets completely
del A
del B

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
'''Преобразование списка в набор удаляет дубликаты, и будут зарезервированы только уникальные элементы.'''
set_age = set(age)
print(set_age)
print(len(age) == len(set_age))
# Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
words = ("I am a teacher and I love to inspire and teach people").split()
set_words = set(words)
print(set_words)
print(len(set_words))
