arr=[9,5,7,2,1,4,3,8,6]
j=1

#Before sorting the array
print("Before sorting the array: ",arr)

for i in range(len(arr)):
	for j in range(len(arr)):
		if arr[i]<arr[j]:
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
		
	
#After the sorting the array
print("After sorting the array:",arr)
		#print(arr[i])
