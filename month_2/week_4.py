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


# Day_51

# Naming Module:You can name the module file whatever you like, but it must have the file extension .py
# Re-naming Module:

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules

import platform
x = platform.system()
print(x)
print(platform.python_version())

#  dir() function.
x = dir(platform)
print(x)

# Import From Module

from mymodule import person1
print(person1["age"])

# Day_52

# Dates in python

import datetime
x = datetime.datetime.now()
print(x)

#Date Output
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Create data object
x = datetime.datetime(2020, 5, 17)
print(x)

# strftime() Method
x = datetime.datetime(2020, 5, 17)
print(x.strftime("%B"))


# Day_53_54

# Task_1

import mymodule

mymodule.sum(1, 8)
mymodule.sub(4, 2)
mymodule.multi(6, 6)
mymodule.divid(8, 2)

# Task_2
import datetime

x = datetime.datetime.now()
print(x.strftime("%c"))

# Task_3

from datetime import datetime, timedelta
# Use timedelta() calculating differences in dates
yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

print(("Yesterday: ") + yesterday.strftime('%Y-%m-%d'))
print(("Tomorrow: ") + tomorrow.strftime('%Y-%m-%d'))

