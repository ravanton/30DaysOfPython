# Creating a Class
# To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.

# # syntax
# class ClassName:
#   code goes here

class Person:
    def __init__(self, firstname, lastname, age, city):
    # self allows to attach parameter to the class
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city



p = Person("Anton", "R", 22, "London")

print(p.lastname)
print(p.firstname)
print(p.age)
print(p.city)

# Object Methods
# Objects can have methods. The methods are functions which belong to the object.
class Person():
    def __init__(self, firstname, lastname, age, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city

    def person_info(self):
        return (f"{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}")

p = Person('Anton', "R", 22, "LA")
print(p.person_info())

# Object Default Methods
# Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:
class Person():
    def __init__(self, firstname = 'Anton', lastname = "R", age = 22, city = "Kiev"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city

    def person_info(self):
        return (f"{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}")

p = Person()
print(p.person_info())
p = Person("Garry", "D", 23, "New york")
print(p.person_info())

# Method to Modify Class Default Values
# In the example below, the person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create add_skill method to add skills to the skills list.
class Person():
    def __init__(self, firstname = 'Anton', lastname = "R", age = 22, city = "Kiev"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city
        self.skills = []

    def person_info(self):
        return (f"{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}")
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('Javascript')
p1.add_skill('Git')
print(p1.skills)

p2 = Person("Garry", "D", 23, "New york")
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheritance
# Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.
class Student(Person):
    
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, city='Helsinki', gender='male'):
        self.gender = gender
        # Overriding parent method
        super().__init__(firstname, lastname,age,city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}.'
    

h1 = Student("Hermiona", "Dginger", 23, "London")
h2 = Student("Ron", "Wizli", 24, "London")
print(h1.person_info())
h1.add_skill('JavaScript')
h1.add_skill('React')
h1.add_skill('Python')
print(h1.skills)

print(h2.person_info())
h2.add_skill('Organizing')
h2.add_skill('Marketing')
h2.add_skill('Digital Marketing')
print(h2.skills)




