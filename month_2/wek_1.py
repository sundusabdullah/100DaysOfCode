
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