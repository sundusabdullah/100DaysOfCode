
# Day_27

# If statements

a = 33
b = 200
if(b > a):
    print("b is greater than a")

# Elif

a = 33
b = 33
if(b > a):
    print("b is greater than a")
elif(a == b):
    print("a and b are equal")

a = 200
b = 33
if(b > a):
    print("b is greater than a")
elif(a == b):
    print("a and b are equal")
else:
    print("a is greater than b")

# Can also have an else without the elif

a = 200
b = 33
if(b > a):
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short hand if ... else

a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a ==b else print("B")

# Use And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")

# Use Or
a = 200
b = 33
c = 500
if a > b or c > a:
    print("At least one of the conditions is true")

# Nested If
x = 41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not have 20.")

# Day_28

# while Loop

i = 1
while i < 6:
    print(i)
    i += 1
# Break statement

i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i += 1

# Continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)

# Else Statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Day_29

# For Loops
fruite = ["apple", "banana", "cherry"]
for x in fruite:
    print(x)

for y in "banana":
    print(y)

# Break statement
fruite = ["apple", "banana", "cherry"]
for x in fruite:
    print(x)
    if x == "banana":
        break

fruite = ["apple", "banana", "cherry"]
for x in fruite:
    if x == "banana":
        break
    print(x)

# Continue statement
fruite = ["apple", "banana", "cherry"]
for x in fruite:
    if x == "banana":
        continue
    print(x)


# Day_30
# range() Function

for x in range(6):
    print(x)

# it is possible to specify the starting value

for x in range(2, 6):
    print(x)

# it is possible to specify the increment value
# 2 is starting value, 30 end value, 2 increment value,
for x in range(2, 30, 3):
    print(x)

# Else in for loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested loop
fruite = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruite:
        print(x, y)

# Day_31

# Creating a Function
def my_function():
    print("Hello from a function")
# calling a function
my_function()

# Parameters
def my_function(fname):
    print(fname + "Refsanes")

my_function("Sundus ")

# Default Parameter Value
def my_function(country = "Norway"):
    print( "I am from " + country)

my_function("Saudi Arabia ")
my_function()

# Day_32_33

A = [3, 5, 7, 9, 11, 13, 15, 17]
B = [2, 4, 6, 8, 10, 12, 14, 16]

for x in A:
    for y in B:
        print(x, y)

# Another way

for x in range(3, 18, 2):
    for y in range(2, 17, 2):
        print(x, y)