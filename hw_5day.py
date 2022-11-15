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

