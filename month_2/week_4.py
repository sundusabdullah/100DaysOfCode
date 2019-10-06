# Day_48

#  Local Scope

def myFunc():
    x = 300
    print(x)
myFunc()

# Function Inside Function
def myFunc():
    x = 300
    def myinnerfunc():
        print(x)

    myinnerfunc()
myFunc()

# Global Scope

x = 300
def myFunc():
    print(x)
myFunc()
print(x)

# Day_49

# Naming Variables

x = 300 # Global

def myFunc():
    x = 200 #local
    print(x)
myFunc()
print(x)

# Global Keyword

def myFunc():
    global x
    x = 300
myFunc()
print(x)

# change to a global variable

x = 300

def myfunc():
    global x
    x = 200

myfunc()
print(x)

# Day_50


# Create a Module: Save code in file .py
# Use a Module: using by import statement after to save file of code
import mymodule
mymodule.greeting(" Sundus")

# Variables in Module

import mymodule

a = mymodule.person1["age"]
print(a)


