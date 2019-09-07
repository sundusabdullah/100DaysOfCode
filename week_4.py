# Day_20

# Empty set
thisset_1 = {}
print(thisset)

thisset_2 = {"apple", "banana", "cherry"}
print(thisset_2)

thisset_3 = {"Ahmad", "Ahmad", 1, 2, 1, 5}
print(thisset_3)

# Access Items
for x in thisset_2:
    print(x)

# Check items in set
print("apple" in thisset_2)


# Add Items
# To add one item use add()
thisset_2.add("orange")
print(thisset_2)

# To add more than one item use update()
thisset_2.update(["orange", "mango", "grapes"])
print(thisset_2)