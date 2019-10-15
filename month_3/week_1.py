
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
