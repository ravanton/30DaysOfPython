# Empty tuple: Creating an empty tuple

# syntax
empty_tuple = ()

# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values

# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Exercises: Day 6
empty_tuple = []
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
name_tuple = [ "Garry", "Rone", "Hermiona", "Draco" ]
name_tuple_new = ["Billy", "Sam", "Piter"]

# Join brothers and sisters tuples and assign it to siblings
join_tupe = name_tuple + name_tuple_new
print("", len(join_tupe))

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ['Banana', 'Orange', 'Mango', 'Lemon']
vegetables = ["Broccoli", "Garlic", "Kale" ]
animal_products = ["Swiss chard", "Green peas"]

# Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list (Измените кортеж about food_stuff_tp на список food_stuff_lt.)
food_stuff_lp = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[4]
print(middle_item)
# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_tp[3:6]
print(first_three_items)

# Полностью удалить кортеж food_staff_tp
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)