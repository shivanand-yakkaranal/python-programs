list1 = ["abc", 34, True, 40, "male"]
list1.append("Shivappa")
print(list1)
list1.reverse()
print(list1)
list1.remove(40)
print(list1)
list1.pop(0)
print(list1)
list2=list1.copy()
print("List2 is copied from list1",list2)

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)