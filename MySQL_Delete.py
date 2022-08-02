# Code by @AmirMotefaker

# MySQL - MySQL Delete From By

# # Solution  1 - Delete Record
# # Delete any record where the address is "Mountain 21"
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# # Output:
# # 1 record(s) deleted



# Solution  2 - Prevent SQL Injection
# Escape values by using the placeholder %s method
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# Output:
# 1 record(s) deleted
