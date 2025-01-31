list1=[1,2,3,4]
list2=[5,6,2,5]
print("List1: ",list1)
print("List2: ",list2)

list3=[]
for x,y in zip(list1,list2):
	list3.append(x+y)

print(list3)
