# Creating a Class
# To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.

# # syntax
# class ClassName:
#   code goes here

class Person:
    def __init__(self, firstname, lastname, age, city):
    # self allows to attach parameter to the class
        # self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city



p = Person("Anton", "R", 22, "London")
# print(p.name)
print(p.lastname)
print(p.firstname)
print(p.age)
print(p.city)
