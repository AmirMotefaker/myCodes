# Code by AmirMotefaker

# MongoDB - Limit

# Limit the Result
# To limit the result in MongoDB, we use the limit() method.
# Limit the result to only return 5 documents:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

for x in myresult:
    print(x)

# Output:
# {'_id': 1, 'name': 'John', 'address': 'Highway37'}
# {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
# {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
# {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
# {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
