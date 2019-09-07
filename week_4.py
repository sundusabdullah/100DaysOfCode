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




# Day_21

# Length of a Set
print(len(thisset_2))

# Remove Item use discard() or remove(), pop()
thisset_2.remove("banana")
print(thisset_2)

# clear() method empties the set
thisset_2.clear()
print(thisset_2)

# set() Constructor

thisset_3 = set(("apple", "banana", "cherry"))
print(thisset_3)