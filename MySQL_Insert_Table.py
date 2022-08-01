# Code by @AmirMotefaker

# MySQL - MySQL Insert Into Table

# # Solution 1 - Insert Into Table
# # Insert a record in the "customers" table
import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="P@ssw0rd",
   database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# # Output:
# # 1 record inserted.



# # Solution 2 - Insert Multiple Rows
# # Fill the "customers" table with data
import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="P@ssw0rd",
   database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

# # Output:
# # 13 was inserted.



# Solution 3 - Get Inserted ID
# Insert one row, and return the ID
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

# Output:
# 1 record inserted, ID: 15
