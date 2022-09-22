# Code by AmirMotefaker

# MySQL - MySQL Create Database

# # Solution 1 - Creating a Database
# # create a database named "mydatabase"
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")



# # Solution 2 - Check if Database Exists
# # Return a list of your system's databases
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# # Output:
# # ('information_schema',)
# # ('mydatabase',)
# # ('mysql',)
# # ('performance_schema',)
# # ('sakila',)
# # ('sys',)
# # ('vision',)
# # ('world',)



# Solution 3 - Try connecting to the database "mydatabase"
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)
