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
