# Day_48

#  Local Scope

def myFunc():
    x = 300
    print(x)
myFunc()

# Function Inside Function
def myFunc():
    x = 300
    def myinnerfunc():
        print(x)

    myinnerfunc()
myFunc()

# Global Scope

x = 300
def myFunc():
    print(x)
myFunc()
print(x)
