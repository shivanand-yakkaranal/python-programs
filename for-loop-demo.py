fruits=["Apple","Mango","Kiwi"]
for i in fruits:
    print(i)

demostring="Banana"
for i in demostring:
    print(i)

#demo range
for i in range(1,10):
    print(i)
else:
    print("Finally finished")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
#------------Nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)