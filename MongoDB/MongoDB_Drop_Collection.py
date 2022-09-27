# Code by @AmirMotefaker

# MongoDB - Drop Collection

# Delete Collection
# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# Delete the "customers" collection:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()
