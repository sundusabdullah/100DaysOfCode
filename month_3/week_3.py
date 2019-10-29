
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
