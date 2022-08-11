# Code by @AmirMotefaker

# MongoDB 

# # Solution 1 - Create Database
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]



# Solution 2 - Check if Database Exists
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

print(myclient.list_database_names())



# Solution 3 - Check if "mydatabase" exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
