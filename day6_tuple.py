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
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ["Broccoli", "Garlic", "Kale" ]
animal_products = ["Swiss chard", "Green peas"]

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
