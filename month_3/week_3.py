
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