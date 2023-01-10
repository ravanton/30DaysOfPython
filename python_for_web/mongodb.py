# Python is a backend technology and it can be connected with different data base applications. It can be connected to both SQL and noSQL databases. In this section, we connect Python with MongoDB database which is noSQL database.
# Connecting Flask application to MongoDB Cluster
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo
from pymongo import MongoClient

MONGODB_URI = ''
client = pymongo.MongoClient(MONGODB_URI)

# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
students = [
        {'name':'David','country':'UK','city':'London','age':22},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)
print(client.list_database_names())
# find students
students = db.students.find()
for student in students:
    print(student)

# Find with Query
query = {
    "country":"UK"
}
students = db.students.find(query)
for student in students:
    print(student)

# remove one John from the collection.
query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)
    
# Using the drop() method we can delete a collection from a database.     
db.students.drop()
app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


