import sys
#Initialize with range
a=range(1,10000)

#Initialize with xrange
#x=xrange(1,10000)

print("The size alloted using range()",sys.getsizeof(a))

# testing the size of x
# xrange() takes less memory
#print("The size alloted using xrange()",sys.getsizeof(x))