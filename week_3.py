
#Day 13

s = []
print(s) # empty List

numbers = [1,2,3,4,5]
print(numbers) #list contains numbers

thislist = ["apple", "banana", "cherry"]
print(thislist) #list contains string

list = ["apple", "banana", "cherry",1,2,3] #list contains string and number
print(list)

num_list = [1.5, 2.5, 3.5]
print(num_list)
print(num_list[1]) #to access items


thislist = ["apple", "banana", "cherry"]
#use for loop to print all item
for i in thislist:
    print(i)

nums_lise = [1.5, 2.5, 3.5, 1,2,3]

for n in nums_lise:
    print(n)

# Change item in list
thislist[1] = "blackcurrant"
print(thislist)

# delete item in list
del thislist[1]
print(thislist)


#Day 14

list_1 = ['A', 'B', 'C', 'D', 'E']
print(list_1[1:3]) #start print from index number 1 and end befor index number 3


#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Repeat Item in List
program_lang = ["Pyrhon"]*4
print(program_lang)

#+ Operator in List
list_2 = ['Ahmad', 'Khalid', 'Omar']
list_3 = ['Sara', 'Hind', 'Batool']
list_4 = list_2 + list_3
print(list_4)

num_1 = [1,2,3,4,5]
num_2 = [1.5, 2.5, 3.5, 4.5, 5.5]
num_3 = num_1 + num_2
print(num_3)

#Day 15

# To count the items in list use len() method.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# To add new item in list use append() method.
thislist.append('orange')

print(thislist)

# To remove specified items in list remove() method.
thislist.remove('banana')
print(thislist)

# To remove specified index in list pop() method.
thislist.pop(1)
print(thislist)

# To remove last item in list.
thislist.pop()
print(thislist)

#To empty list use clear()
thislist.clear()
print(thislist)

# To copy list copy() method.
mylist = thislist.copy()
print("Copy list:", mylist)

# use list() function to make a new list.
language = list(("python", "php", "js"))
print(language)

# Day 16
# Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple_2 = ()
# will print empty tuple
print(thistuple_2)


# When definition one element must put a comma
thistuple_3 = (3,)
print(thistuple_3)

thistuple_4 = ("Sundus", 1.1, 4, "Python")
print(thistuple_4)
# Access Tuple Items
print(thistuple_4[0])
# Loop Through a Tuple
for i in thistuple_4:
    print(i)

# Add new Items
thistuple_4[4] = "Abdullah"
# will give error because the tuple unchangeable
print(thistuple_4)

# print items from index 0 to index 2
print(thistuple_4[0:3])


# Day 17

#Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple ")

# Repeat Item
thistuple_2 = ("python",) * 3
print(thistuple_2)

# + Operator
thistuple1 = (1, 2, 3, 4)
thistuple2 = (5, 6)
thistuple3 = thistuple1 + thistuple2
print(thistuple3)

x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)

# Tuple Length
print(len(thistuple))

# tuple() Constructor

thistuple_3 = tuple(("PHP", "Java", "Python"))
print(thistuple_3)

thislist = [3, 4, 5, 6, "A", "B"]
thistuple_4 = tuple(thislist)
print(thistuple_4)