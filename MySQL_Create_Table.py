# Code by @AmirMotefaker

# MySQL - MySQL Create Table

# # Solution 1 - Creating a Table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



# # Solution 2 - Check if Table Exists
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# # Output:
# # ('customers',)



# # Solution 3 - Primary Key
# # Create primary key when creating the table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



# Solution 4 - Primary Key
# If the table already exists, use the ALTER TABLE keyword:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
