
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
    

    result_str = ''.join(random.choice("abcd345gkd967bpl") for i in range(7))
    return result_str
print(random_user_id())

    

