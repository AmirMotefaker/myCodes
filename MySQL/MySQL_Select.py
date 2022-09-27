# Code by AmirMotefaker

# MySQL - MySQL Select From

# # Solution 1 - Select From a Table
# # Select all records from the "customers" table, and display the result
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# # Output:
# # ('John', 'Highway 21', 1)
# # ('Peter', 'Lowstreet 4', 2)  
# # ('Amy', 'Apple st 652', 3)   
# # ('Hannah', 'Mountain 21', 4) 
# # ('Michael', 'Valley 345', 5) 
# # ('Sandy', 'Ocean blvd 2', 6) 
# # ('Betty', 'Green Grass 1', 7)
# # ('Richard', 'Sky st 331', 8) 
# # ('Susan', 'One way 98', 9)   
# # ('Vicky', 'Yellow Garden 2', 10)
# # ('Ben', 'Park Lane 38', 11)
# # ('William', 'Central st 954', 12)
# # ('Chuck', 'Main Road 989', 13)
# # ('Viola', 'Sideway 1633', 14)
# # ('Michelle', 'Blue Village', 15)



# # Solution 2 - Selecting Columns
# # Select only the name and address columns
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# # Output:
# # ('John', 'Highway 21')
# # ('Peter', 'Lowstreet 4')
# # ('Amy', 'Apple st 652')
# # ('Hannah', 'Mountain 21')
# # ('Michael', 'Valley 345')
# # ('Sandy', 'Ocean blvd 2')
# # ('Betty', 'Green Grass 1')
# # ('Richard', 'Sky st 331')
# # ('Susan', 'One way 98')
# # ('Vicky', 'Yellow Garden 2')
# # ('Ben', 'Park Lane 38')
# # ('William', 'Central st 954')
# # ('Chuck', 'Main Road 989')
# # ('Viola', 'Sideway 1633')
# # ('Michelle', 'Blue Village')


# Solution 3 - Using the fetchone() Method
# Fetch only one row
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

# Output:
# ('John', 'Highway 21', 1)
