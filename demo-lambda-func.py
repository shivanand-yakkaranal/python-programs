mul=lambda a,b:a+b
print(mul(1,2))

def wrapper(n):
    return lambda a:a+n

myFun=wrapper(10)
content=myFun(2)
print(content)
