
# Day_62


# PIP is Installed
#  If you have Python version 3.4 or later, PIP is included by default.

# Using a Package
import camelcase
c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))

# Remove a Package
# Use uninstall to remove a package

#  List Packages
# Use Pip list



# Day_63

# Command Line Input

print("Enter your name: ")
x = input()
print("Hello", x)

# Day_64

# Exception Handling
try:
    print(x)
except:
    print("An exception occurred")

# This statement will raise an error, because x is not defined
print(x)

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else

try:
    print("Hello")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")


# Finally

try:
    print(x)
except:
    print("Something  went wrong")
finally:
    print("The 'try except' is finished")

# Day_65

# String format()

prince = 49
txt = "The price is {} dollars"
print(txt.format(prince))

# Format the price to be displayed as a number with two decimals.

prince = 49
txt = "The price is {:.2f} dollars"
print(txt.format(prince))

# Multiple Values

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, prince))