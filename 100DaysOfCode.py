

# First/ Second Day...

#the print method uses to print anything on the screen
print("Hello World")

"""
can use Relational
Operators in python
"""
if 5 > 2:
    print("Five is greater than two!")


#Third day

#Python has no command for declaring a variable

x = 5 # x is integer
y = "Sundu" # y is string
print(x)
print(y)

#In Python single or double quotes is same

y = 'Sundus'
z = "Sundus"

#Assign Value to Multiple Variables
x,y,z = "sundus", "Abdullah", "IT"
print(x,y,z)

#Output Variables
x = "awesome"
print("python is " + x)

#or, To use combine + must variables have the same type

x = "awesome"
y = "python is "
print(y + x)


#Fourth Day


x = 1
y = 2.8
z = 1j

#use type() function to define the type of variable
print(type(x)) #int
print(type(y)) #float
print(type(z)) #complex


x = 1
y = 2.8
z = 1j

# convert from int to float

a = float(x)

# convert from float to int

b = int(y)

# convert from int to complex

c = complex(x)

print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))


# To print random number

import random

print(random.randrange(1,10))


