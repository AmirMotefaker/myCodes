# Code by AmirMotefaker

# MongoDB - Update

# Update Collection
# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# Change the address from "Valley 345" to "Canyon 123"
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)

# Output:
# {'_id': 1, 'name': 'John', 'address': 'Highway37'}
# {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
# {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
# {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
# {'_id': 5, 'name': 'Michael', 'address': 'Canyon 123'}
# {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
# {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
# {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
# {'_id': 12, 'name': 'William', 'address': 'Central st 954'}
# {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}



# Update Many
# To update all documents that meets the criteria of the query, use the update_many() method.
# Update all documents where the address starts with the letter "S":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# Output:
# 2 documents updated.
