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


