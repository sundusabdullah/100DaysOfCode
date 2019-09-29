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
