#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *

#https://www.w3schools.com/python/python_mongodb_getstarted.asp

#switch to my database
mydb = client['spq4pq']

#create a new collection
newcoll = mydb["newcoll"]

#clear documents from collection to prevent re-adding documents: 
clear = newcoll.delete_many({})


#create new documents 
documents = []

student_1 = {
    "student info": {
      "name": "John Jackson",
      "classes": [
        "math",
        "science"
      ],
      "GPA": 3.4,
    },
    "address": "123 West Street",
}

student_2 = {
    "student info": {
      "name": "Easton Lee",
      "classes": [
        "religion",
        "health",
        "science",
        "spanish"
      ],
      "GPA": 3.1,
    },
    "address": "8 Oak Street",
}

student_3 = {
    "student info": {
      "name": "Bree Wilson",
      "classes": [
        "german",
        "history"
      ],
      "GPA": 2.1,
    },
    "address": "111 Grand Tree",
}

student_4 = {
    "student info": {
      "name": "Will Johnny",
      "classes": [
        "math",
        "science",
        "literature",
        "french"
      ],
      "GPA": 3.9,
    },
    "address": "22 East Way",
}

student_5 = {
    "student info": {
      "name": "Allison Earl",
      "classes": [
        "biology",
        "chemistry",
      ],
      "GPA": 1.9,
    },
    "address": "1 Middle Way",
}

documents.append(student_1)
documents.append(student_2)
documents.append(student_3)
documents.append(student_4)
documents.append(student_5)

# Insert new records
newcoll.insert_many(documents)

#display three of the documents 
#query to get students with gpa > 3.0
get_students = newcoll.find({"student info.GPA": {"$gt": 3.0}})

for student in get_students:
    print(f'{student}\n')