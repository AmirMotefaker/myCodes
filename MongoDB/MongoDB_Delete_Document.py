# Code by AmirMotefaker

# MongoDB - Delete Document

# # Delete Document
# # To delete one document, we use the delete_one() method.
# # Delete the document with the address "Mountain 21":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

for x in mycol.find():
    print(x)

# # Output:
# # {'_id': ObjectId('62f9e1a88fba368ee198c4b0'), 'name': 'John', 'address': 'Highway 37'}
# # {'_id': ObjectId('62f9e1c5192156652f8e118f'), 'name': 'Peter', 'address': 'Lowstreet 27'}
# # {'_id': ObjectId('62f9e1d6297980eb28d86434'), 'name': 'Amy', 'address': 'Apple st 652'}  
# # {'_id': ObjectId('62f9e1d6297980eb28d86436'), 'name': 'Michael', 'address': 'Valley 345'}
# # {'_id': ObjectId('62f9e1d6297980eb28d86437'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# # {'_id': ObjectId('62f9e1d6297980eb28d86438'), 'name': 'Betty', 'address': 'Green Grass 1'}
# # {'_id': ObjectId('62f9e1d6297980eb28d86439'), 'name': 'Richard', 'address': 'Sky st 331'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643a'), 'name': 'Susan', 'address': 'One way 98'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643b'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643c'), 'name': 'Ben', 'address': 'Park Lane 38'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643d'), 'name': 'William', 'address': 'Central st 954'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643e'), 'name': 'Chuck', 'address': 'Main Road 989'}
# # {'_id': ObjectId('62f9e1d6297980eb28d8643f'), 'name': 'Viola', 'address': 'Sideway 1633'}
# # {'_id': 1, 'name': 'John', 'address': 'Highway 37'}
# # {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
# # {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
# # {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
# # {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# # {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
# # {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
# # {'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
# # {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# # {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
# # {'_id': 12, 'name': 'William', 'address': 'Central st 954'}
# # {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
# # {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}



# Delete Many Documents
# To delete more than one document, use the delete_many() method.
# Delete all documents were the address starts with the letter S
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted")

# Output:
# 4 documents deleted



# Delete All Documents in a Collection
# To delete all documents in a collection, pass an empty query object to the delete_many() method:
# Delete all documents in the "customers" collection
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

# Output:
# 11 documents deleted.
