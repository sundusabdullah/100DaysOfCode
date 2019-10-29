
# day_69

#  open() function
f = open("hello.txt", "rt")

# Open a File on the Server

f = open("hello.txt", "r")
print(f.read())

# Read Only Parts of the File

print(f.read(5))

# Read Lines
print(f.readline())

# Close Files
f.close()

# Write to an Existing File

f = open("hello.txt", "a")
f.write("Now this file has more content!")
f.close()

f = open("hello.txt", "r")
print(f.read())

# Create a New File
f = open("myfile.txt", "x")

# Delete a File
import os
os.remove("myfile.txt")

# Check if File exist

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exite")

# Delete Folder

os.rmdir("myfolder")


# day_70

import mysql.connector

# creating a connection

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="12345678",
    db="mydatabase"
)
print(mydb)

# Creating a Database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print (x)

# Creating a Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print (x)

# Primary Key
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# Day_71

# Insert Into Table

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Insert Multiple Rows
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

# Get Inserted ID
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Sundus", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

# Select From
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Selecting Columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# fetchone() Method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# Select With a Filter
sql = "SELECT * FROM customers WHERE name = 'sundus'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Wildcard Characters
sql = "SELECT * FROM customers WHERE address Like '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)