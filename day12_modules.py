
# mymodule.py file

def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname




# # import the module
# import os
# # Creating a directory
# # os.mkdir('directory_name')
# # Changing the current directory
# os.chdir('path')
# # Getting current working directory
# os.getcwd()
# # Removing directory
# os.rmdir()
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

from math import pi as  PI
print(PI) # 3.141592653589793

# Writ a function which generates a six digit/character random_user_id
import random

def random_user_id():
    
    result_str = ''.join(random.choice("abcd345gkd967bpl") for i in range(6))
    return result_str

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def  user_id_gen_by_user():

    number_of_characters = int(input("Enter number of characters: "))
    number_of_IDs = int(input("Enter number of IDs: "))

    for r in range(number_of_characters):
        result_character = ''.join([random.choice("AWS95rESbmXSAer1234567") for i in range(number_of_IDs)])
        print(result_character)
    # return result_character
    
print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).


