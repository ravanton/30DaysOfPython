#List of Dictionaries
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Garry", "house":"Griffindor","patronus":"Stag"},
    {"name":"Ron", "house":"Griffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None}
]
 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
   