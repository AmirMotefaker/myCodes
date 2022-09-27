# Code by AmirMotefaker

# MongoDB - Query


# Solution 1 - Filter the Result
# The first argument of the find() method is a query object, and is used to limit the search.
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Output:
# {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}




# Solution 2 - Advanced Query
# To make advanced queries you can use modifiers as values in the query object.
# to find the documents where the "address" field starts with the letter "S" or
# higher (alphabetically), use the greater than modifier: {"$gt": "S"}
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Output:
# {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
# {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}




# Solution 3 - Filter With Regular Expressions
# To find only the documents where the "address" field starts with the letter "S",
# use the regular expression {"$regex": "^S"}
## Regular expressions can only be used to query strings.

# Find documents where the address starts with the letter "S"
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Output:
# {'_id': 10, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
