# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary
# To create a dictionary we use curly brackets, {} or the dict() built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Example:

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4    

"""Доступ к элементу по имени ключа вызывает ошибку, если ключ не существует. Чтобы избежать этой ошибки, сначала мы должны проверить, существует ли ключ, или мы можем использовать метод get . Метод get возвращает None, который является типом данных объекта NoneType, если ключ не существует. """
print(person.get('age'))
print(person.get('name'))

# Adding Items to a Dictionary
person['job_title'] = 'Developer'
person['skills'].append('Git')
print(person)

# Exercises: Day 8
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Bim',
    'color': 'black',
    'breed': 'bigle',
    'legs':'middle',
    'age': 6

}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'Anton',
    'last_name': 'Rud',
    'gender': 'male',
    'age': 22,
    'marital_status': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Great Britan',
    'city': 'Manchester',
    'address': {
        'street': 'Westham street',
        'zipcode': '032321'
    }
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

# Modify the skills values by adding one or two skills
student['skills'] = ['Git', 'Python3']

print(student)
# Get the dictionary keys as a list
keys = student.keys()
print(keys)
# Get the dictionary values as a list
values = student.values()
print(values)
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.pop('age')
print(student)
# Delete one of the dictionaries
del dog