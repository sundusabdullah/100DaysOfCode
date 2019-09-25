# Day_34

# Passing a list as a parameter

def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Cherry"]
my_function(fruits)

# Return Values

def my_function(x):
    return  5 * x

print (my_function(3))
print (my_function(5))
print (my_function(9))

# Keyword Arguments

def my_function(child3, child2, child1):
    print ("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Arguments

def my_function(*kida):
    print ("The youngest child is " + kida[2])

my_function("Emil", "Tobias", "Linus")

# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print ("\n\n Recursion Example Result")
tri_recursion(6)

# Day_35

#lambda function()
x = lambda a: a + 10
print(x(5))

# lambda function that multiplies argument
x = lambda a, b: a*b
print(x(5, 6))

# lambda function that sums argument

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# Day_36

def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(3)
print(mydoubler(11))


def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# Day_37
# Arrays

cars = ["Ford", "Volvo", "BMW"]
print(cars)

#  Access the Elements of an Array

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# Modify the value

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

# Length of an Array

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# Day_38

# Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# Adding Array Elements
cars.append("Honda")
print(cars)

#Removing Array Elements, pop() method
cars.pop(1)
print(cars)

#remove() method
cars.remove("Volvo")
print(cars)