
# Day_55

# JSON

import json

x = '{ "name":"Sundus", "age":26, "city":"Saudi Arabia"}'
y = json.loads(x)
print(y["age"])

# Convert from Python to JSON

x = {
    "name":"Sundus",
    "age":26,
    "city":"Saudi Arabia"
}
y = json.dumps(x)
print(y)

# Example

x = {
    "name":"Sundus",
    "age":26,
    "married": False,
    "divorced": False,
    "pets": None,
    "city":"Saudi Arabia",
    "cars":[
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"Ford", "mpg": 24.5}
    ]
}
y = json.dumps(x)
print(y)

# Day_56
#Format the result

import json
x = {
    "name":"Sundus",
    "age":26,
    "married": False,
    "divorced": False,
    "pets": None,
    "city":"Saudi Arabia",
    "cars":[
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"Ford", "mpg": 24.5}
    ]
}
# Use the indent
print(json.dumps(x, indent=4))

# Use the separators
print(json.dumps(x, separators=(". ", " = ")))

# Use the sort_keys
print(json.dumps(x, sort_keys=True))


# Day_57

# RegEx Module

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if(x):
    print("Yes, We have a match!")
else:
    print("No match")


# Metacharacters
y = re.findall("[a-f]", txt)
print(y)

z = re.findall("\S", txt)
print(z)

S = re.findall("\W", txt)
print(S)

# Day_58

# findall() Function
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

if(x):
    print("Yes, there is at least one match")
else:
    print("No match")

# search() Function

y = re.search("\s", txt)
print("The first white-space character is located in position:", y.start())

z = re.split("\s", txt)
print(z)

# Day_59

# sub() Function

import re

str = "The rain in Spain"
# Replace every white-space character with the number 9
x = re.sub("\s", "9", str)
print(x)


# Replace the first 2white-space with the number 9
x = re.sub("\s", "9", str, 2)
print(x)

# Match Object

x = re.search("ai",  str, 2)
print(x)

# Print the position (start- and end-position) of the first match occurrence

x = re.search(r"\bS\w+", str)
print(x.span())

# Print the part of the string where there was a match.
x = re.search(r"\bS\w+", str)
print(x.group())