
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
import random

def  user_id_gen_by_user():

    number_of_characters = int(input("Enter number of characters: "))
    number_of_IDs = int(input("Enter number of IDs: "))

    for r in range(number_of_characters):
        result_character = ''.join([random.choice("AWS95rESbmXSAer1234567") for i in range(number_of_IDs)])
        print(result_character)
    # return result_character
    
print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
    
    for i in range(3):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = (r,g,b)
    return rgb
print(f"rgb{rgb_color_gen()}")

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


import random


def gen_random_hex_color():
    hex_digits = '0123456789ABCDEF'

    return '#' + ''.join(
        random.choices(hex_digits, k=6)
    )
print(gen_random_hex_color())

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random
def list_of_rgb_colors(number):
    rgb_color = []

    
    for i in range(number):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rgb = (r,g,b)
        # rgb_color.append("rgb"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
            rgb_color.append(rgb)
    return rgb_color
print(list_of_rgb_colors(3))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list():
    list = ["apple", "mango", "watermelow"]
    random.shuffle(list)

    return list

print(shuffle_list())

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def gen_random_number_in_range(low, high, n):
    a_list = list(range(low, high))

    random.shuffle(a_list)
    return a_list[:n]
print(gen_random_number_in_range(0, 9, 7))