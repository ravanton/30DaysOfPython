# Declare an empty list
empty_list = []
# Declare a list with more than 5 items
list_5_item = ["web3", "python3", "js", "bitcoin", "git"]

# Find the length of your list
print("Length my list: ", len(list_5_item))

# Get the first item, the middle item and the last item of the list
first_item = list_5_item[0]
middle_item = list_5_item[2]
last_item = list_5_item[-1]
print(last_item)
print(first_item)
print(middle_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Anton", 22, "183 cm", "men", "Usa, NY"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Hulu"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

# Add an IT company to it_companies
it_companies.append("PandaDoc")

# Insert an IT company in the middle of the companies list
it_companies.insert(3, "EPAM")

# Join the it_companies with a string '#;  '
print("#; ".join(it_companies))

# hash = "#; ".join(it_companies)
# print(hash)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[3:9])
# Slice out the last 3 companies from the list
print(it_companies[0:6])
#  Slice out the middle IT company or companies from the list
print(it_companies[3:5])
# Remove the first IT company from the list
del it_companies[0]
# Remove the middle IT company or companies from the list
del it_companies[4]
# Remove the last IT company from the list
del it_companies[-1]
# Remove all IT companies from the list
it_companies.clear()
# Destroy the IT companies list
del it_companies

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
print(full_stack)
full_stack.insert(5, "Python3")
full_stack.insert(6, "SQL")

print(full_stack)

# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Отсортируйте список и найдите минимальный и максимальный возраст
ages.sort()
max_ages = max(ages)
min_ages = min(ages)
print(max_ages)

ages.append(19)
ages.append(26)

# Найдите средний возраст (сумма всех предметов, деленная на их количество)
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range_ages = max(ages) - min(ages)
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
min_average_age = abs((max_ages) / len(ages))
max_average_age = abs((min_ages) / len(ages))
print(min_average_age)
print(max_average_age)
print(max_average_age == min_average_age)

#  Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
Ch, Ru, Us, *scandic = countries
print("Scandic countries: ", scandic)

