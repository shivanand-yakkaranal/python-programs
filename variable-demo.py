"""
a=10
print(type(a))
b="Demo"
print(type(b))
"""
#Python allows you to assign values to multiple variables in one line:
"""
x,y,z="Hello","World",101
print(x)
print(y)
print(z)
"""
#And you can assign the same value to multiple variables in one line:
"""
a=b=c="Hello World"
print(a)
print(b)
print(c)
"""
#Unpack a Collection
"""
fruits=["Apple","Banana","Orange"]
x,y,z=fruits
print(x)
print(y)
print(z)
"""
#In the print() function, you output multiple variables, separated by a comma:
"""
x=110
y=210
z=300
print(x,y,z)
"""
#You can also use the + operator to output multiple variables:
"""
a="Python "
b="is "
c="awsome"
print(a+b+c)
"""
#For numbers, the + character works as a mathematical operator:
"""
a=10
b=20
print(a+b)
"""
#Fibonocice series
"""
a=0
b=1
print(a)
print(b)
for i in range(8):
    c=a+b
    a=b
    b=c

    print(c)
   """
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""
a=10
y="hell"
print(a+b)
"""
#Create a variable outside of a function, and use it inside the function
"""
x="awesome"
def myFun():
    print("Python is "+x)

myFun()
"""
#Create a variable inside a function, with the same name as the global variable
"""
x="awesome"
def myFun():
    x="Fantastic"
    print("Python is "+x)

myFun()
print("Python is "+x)
"""
"""
#If you use the global keyword, the variable belongs to the global scope:
def myFun():
    global x
    x="Fantastic"

myFun()
print("Python is "+x)
"""
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
x="awesome"
def myFun():
    global x
    x="Fantastic"
myFun()
print("Python is "+x)
"""
a="Hello"
b="World"
print(a,b)
