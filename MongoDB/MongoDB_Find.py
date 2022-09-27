# Code by AmirMotefaker

# MongoDB - Find

# # Solution 1 - Find One
# # The find_one() method returns the first occurrence in the selection.
# # Find the first document in the customers collection
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)



# # Solution 2 - Find All
# # To select data from a table in MongoDB, we can also use the find() method.
# # The find() method returns all occurrences in the selection.
# # Return all documents in the "customers" collection, and print each document
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)



# Solution 3 - Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result.
# This parameter is optional, and if omitted, all fields will be included in the result.
# Return only the names and addresses, not the _ids
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)



# Solution 4 
# This example will exclude "address" from the result:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)
