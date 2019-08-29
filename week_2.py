# Sixth Day

# All outputs become int type

x = int(1)
y = int(2.8)
z = int("3")
print(x,"\n", y,"\n",z)


# All outputs become float type

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x,"\n", y,"\n",z,"\n",w)


# All outputs become string type

x = str("s1")
y = str(2)
z = str(3.0)
print(x,"\n", y,"\n",z)





# Seventh Day

# To display a string use print() function
# will print same result
print('Hello')
print("Hello")

# Assign String to a Variable

a = "Hello"
print(a) # output = Hello

#  Multiline Strings

a = '''
Python is an interpreted, object-oriented, high-level programming
 language with dynamic semantics. Its high-level built 
 in data structures
'''

print(a)


a = "Hello, World!"

print(a[1]) # output = e
print(a[2:5]) # output = llo

# Eighth Day

# strip() use to removes whitespace from the beginning or the end
a = " Hello, World "
print(a.strip())

# len() method returns the length of a string.
print("the length of a string is:", len(a))

# lower() method returns the string in lower case.
print(a.lower())

# upper() method returns the string in upper case.
print(a.upper())

#  replace() method replaces a string with another string.
print(a.replace('World','sundus'))

# split() method splits the string into substrings
print(a.split(","))


#Ninth Day

age = 36
#txt = "My name is sundus, I am " + age
#print(txt) # Error in output because cannot combine strings and numbers.

txt_2 = "My name is sundus, I am {}"
# We can combine strings and numbers by using the format() method
print(txt_2.format(age))

quantity = 3
itemno = 567
price = 49.95

myOrder = " I want {} pieses of item {} for {} dollars."
print(myOrder.format(quantity, itemno, price))

'''You can use index numbers {0} to be sure the arguments are placed in the
￼correct placeholders'''

myOrder_2 = " I want to pay {2} dollars for {0} pieses of item {1}."
print(myOrder_2.format(quantity, itemno, price))


# Tenth Day

"""Arithmetic operators are used with numeric values to perform common
 mathematical operations."""

x = 5
y = 3
print(x * y)


# x = x / 3
x /= 3
# x = x + 3
x += 3
print(x)

# Comparison Operators output true or false

print(x < y) # false
print(x != y) #true

# Eleventh Day

# Logical Operators, output true or false

z = 5
print(z > 3 or z < 4) #true

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]

z = x

#Identity Operators
print(x is not z) #false
print(x is not y) #true
print(x != y) #false

#Membership Operators
print("banana" in x) #true
print("oranges" in x) #false


# Task_2

text_2 = "Please, I want {} sandwishes and {} donutes"
num_1 = 5
num_2 = 7


# use replace() function
print(text_2.replace("I", "we"))

# use format() function
print(text_2.format(num_1, num_2))

# use replace() function
print(text_2.replace("a", "A"))

# print text after performing all changes.
print(text_2.replace("I", "we").format(num_1, num_2).replace("a", "A"))

