# Code by @AmirMotefaker

# MySQL - MySQL Connection

# # Solution 1 - Test MySQL Connector
# import mysql.connector



# Solution 2 - Create Connection 
# Use the username and password from your MySQL database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd"
)

print(mydb)

# Output:
# <mysql.connector.connection_cext.CMySQLConnection object at 0x00000258A3E746D0>
