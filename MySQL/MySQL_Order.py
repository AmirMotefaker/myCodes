# Code by AmirMotefaker

# MySQL - MySQL Order By

# # Solution 1 - Sort the Result
# # Sort the result alphabetically by name
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# # Output:
# # ('Amy', 'Apple st 652', 3)
# # ('Ben', 'Park Lane 38', 11)
# # ('Betty', 'Green Grass 1', 7)
# # ('Chuck', 'Main Road 989', 13)
# # ('Hannah', 'Mountain 21', 4)
# # ('John', 'Highway 21', 1)
# # ('Michael', 'Valley 345', 5)
# # ('Michelle', 'Blue Village', 15)
# # ('Peter', 'Lowstreet 4', 2)
# # ('Richard', 'Sky st 331', 8)
# # ('Sandy', 'Ocean blvd 2', 6)
# # ('Susan', 'One way 98', 9)
# # ('Vicky', 'Yellow Garden 2', 10)
# # ('Viola', 'Sideway 1633', 14)
# # ('William', 'Central st 954', 12)



# Solution 2 - ORDER BY DESC
# Sort the result reverse alphabetically by name
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Output:
# ('William', 'Central st 954', 12)
# ('Viola', 'Sideway 1633', 14)
# ('Vicky', 'Yellow Garden 2', 10)
# ('Susan', 'One way 98', 9)
# ('Sandy', 'Ocean blvd 2', 6)
# ('Richard', 'Sky st 331', 8)
# ('Peter', 'Lowstreet 4', 2)
# ('Michelle', 'Blue Village', 15)
# ('Michael', 'Valley 345', 5)
# ('John', 'Highway 21', 1)
# ('Hannah', 'Mountain 21', 4)
# ('Chuck', 'Main Road 989', 13)
# ('Betty', 'Green Grass 1', 7)
# ('Ben', 'Park Lane 38', 11)
# ('Amy', 'Apple st 652', 3)
