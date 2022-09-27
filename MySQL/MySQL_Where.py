# Code by @AmirMotefaker

# MySQL - MySQL Where

# # Solution 1 - Select With a Filter
# # Select record(s) where the address is "Park Lane 38"
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# # Output:
# # ('Ben', 'Park Lane 38', 11)



# # Solution 2 - Wildcard Characters
# # Select records where the address contains the word "way"
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# # Output:
# # ('John', 'Highway 21', 1)
# # ('Susan', 'One way 98', 9)
# # ('Viola', 'Sideway 1633', 14)



# Solution 3 - Prevent SQL Injection
# Escape query values by using the placholder %s method:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Output:
# ('Vicky', 'Yellow Garden 2', 10)
