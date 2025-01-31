import copy
import sys
x=[[1,2,3],4,5]
# Printing the list values
print("List before copy and deepcopy operations: ",x)
'''y=copy.copy(x)
y[0][0]=6
print(x,y)'''
print("After update to ")

#Print the array after shallow copy
#print("After the shallow copy:",y)
z=copy.deepcopy(x)
z[0][0]=9
#Print the array after deepcopy
print("After the deepcopy:",z)
print(x)
'''
objref=sys.getrefcount(x)
print(objref)
'''