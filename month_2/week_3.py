# Day_41

# Create a Class

class Myclass:
    x = 5
print(Myclass)

# Create Object

class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)

class Person():
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("sundus", 26)
p1.myFunc()


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("sundus", 26)
print(p1.name)
print(p1.age)

# Day_42

# Object Methods

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
       print("Hello my name is " + self.name)
p1 = Person("sundus", 26)
p1.myFunc()

# Modify Object Properties

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
       print("Hello my name is " + self.name)
p1 = Person("sundus", 26)
p1.age = 40
print(p1.age)

# Delete Object Properties

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
       print("Hello my name is " + self.name)
p1 = Person("sundus", 26)
del p1.age
print(p1.age) #Error: AttributeError: 'Person' object has no attribute 'age'

# Delete Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
       print("Hello my name is " + self.name)
p1 = Person("sundus", 26)
del p1
print(p1) # NameError: name 'p1' is not defined


# Day_43
# Python Inheritance
# Create a Parent Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)
x = Person("sundus", "Abdullah")
x.printname()


# Create a Child Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

# Child Class
class Student(Person):
    pass

x = Student("sundus", "Abdullah")
x.printname()

# Add the __init__() function

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("sundus", "Abdullah")
x.printname()

# Day_44