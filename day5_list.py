#Unpacking List Items
item = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = item
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest) 

# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Adding Items to a List
# syntax
# lst = list()
# slst.append(item)


fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# Inserting Items into a List

# syntax
# lst = ['item1', 'item2']
# lst.insert(index, item)

fruits.insert(2, "watermellon")
print(fruits)

# Joining Lists
# syntax
# list3 = list1 + list2
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Joining using extend() method The extend() method allows to append list in a list. See the example below.
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

# Sorting List Items
# sort(): this method modifies the original list

# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
