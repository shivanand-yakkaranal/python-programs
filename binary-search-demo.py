def binary_search(arr,target):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2 # Find the middle index
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            high=mid-1
        
        else:
            low=mid+1
    return -1 #Element is not present in the array

arr=[1,3,5,7,9,11,13,15,17,19]
target=7

result=binary_search(arr,target)

if result!=-1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")