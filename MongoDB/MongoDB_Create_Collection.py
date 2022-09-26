# Code by AmirMotefaker

# MongoDB - Create Collection

# # Solution 1 - Creating a Collection
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]



# # Solution 2 - Check if Collection Exists
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]

print(mydb.list_collection_names())



# Solution 3 - Check if the "customers" collection exists
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
