# syntax
# IF condition:
    # this part of code runs for truthy conditions

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

# IF ELSE
# syntax
# if condition:
    # this part of code runs for truthy conditions
# else:
    #  this part of code runs for false conditions

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
years = int(input("Enter your age: "))
years_learn_to_driver = 18 - years

if years >= 18:
    print("You are old enough to drive.\nOutput:") 
else:
    print(f"You need {years_learn_to_driver} more years to learn to drive.")

# 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
your_age = int(input("Enter your afe: "))
my_age = 22
older_me = your_age - my_age
if my_age == your_age:
    print("Yep it's my years!")
else:
    print(f"You are {older_me} years older than me.")