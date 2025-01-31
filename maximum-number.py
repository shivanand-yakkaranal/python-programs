arrNum=[1,22,44,775,120,244,3,46,75]
print("NUmber list: ",arrNum)
maxnum=arrNum[0]
for num in arrNum:
	if num>maxnum:
		maxnum=num

print(maxnum)