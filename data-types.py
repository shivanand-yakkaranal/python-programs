import re
"""
#To get the data type of any object using type() function
x=10
print(type(x))
"""
# setting the data types
#str
x="Hello World"
print(type(x))

# Numeric
x=11
y=10.5
z=1j
print(type(x),type(y),type(z))


"""
Sequence
"""
#print(re.__doc__)
x = ["apple", "banana", "cherry"]
print(type(x))
x =("apple","banana","cherry")
print(type(x))
x=range(6)
print(type(x))