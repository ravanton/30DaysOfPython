fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruits = input("Enter you'r fruits: ")

if new_fruits  not in fruits:
    print(f"That are new fruits add to list: {fruits.append(new_fruits)}", (fruits))
else:
    print("That fruit already exist in the list")