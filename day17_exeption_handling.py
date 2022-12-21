# try:
#     code in this block if things go well 
#     код в этом блоке, если все идет хорошо
# except:
#     code in this block run if things go wrong
# код в этом блоке выполнить, если все пойдет не так

try:
    print(10 + '5')
except:
    print('Something went wrong')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')
# else:
#     print("I usually run with the try block")
# finally:
#     print("I alway run.")

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# Packing and Unpacking Arguments in Python
# We use two operators:

# * for tuples
# ** for dictionaries
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

# Enumerate
# If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.
countries = ['Finland', 'Sweden', 'Norway']

# for index, item in enumerate([20, 30, 40]):
#     print(index, item)


for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')

# Zip

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_vegetables = []

for h, v in zip (fruits, vegetables):
    fruits_and_vegetables.append({'fruits':h, 'veg':v})
print(fruits_and_vegetables)