# Code by @AmirMotefaker

# MySQL - MySQL Join

# Solution 1 - Join Two or More Tables
# Join users and products to see the name of the users favorite product
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



# Solution 2 - LEFT JOIN
# Select all users and their favorite product:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



# Solution 3 - RIGHT JOIN
# Select all products, and the user(s) who have them as their favorite
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
