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

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
years = int(input("Enter your age: "))
years_learn_driver = 18 - years
if years >= 18:
    print("You are old enough to drive.\nOutput:") 
else:
    print(f"You need {years_learn_driver} more years to learn to drive.")