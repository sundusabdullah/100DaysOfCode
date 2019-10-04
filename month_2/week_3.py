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

# super() Function

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("sundus", "Abdullah")
x.printname()

# Add Properties

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2018

x = Student("sundus", "Abdullah")
print(x.graduationyear)

# Add parameter

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("sundus", "Abdullah", 2018)
print(x.graduationyear)

# Add Methods

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
       print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("sundus", "Abdullah", 2018)
x.welcome()


# Day_45

# Iterator

mytuple = ("Apple", "Banana", "Cherry")

myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mtstr = "Banana"
myit = iter(mtstr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



# Looping Through an Iterator

for x in mytuple:
    print(x)

for x in mtstr:
    print(x)

# Create an Iterator

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x

        else:
            raise StopIteration

myclass = MyNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)

# Day_46_47


class library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

    def printinfo(self):
        print( self.book, self.shelf)

x = library(300, 45)
x.printinfo()
class science_section(library):
    def __init__(self, book, shelf, name ):
        super().__init__(book, shelf)
        self.name = name

    def printinfo(self):
        print("Number of books is", self.book, ",and number of shelf", self.shelf, "one of the books is",self.name)

y = science_section(20, 4, "Physics book") #object
y.printinfo()