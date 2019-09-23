# Day_34

# Passing a list as a parameter

def my_function(food):
    for x in food:
        print (x)

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

