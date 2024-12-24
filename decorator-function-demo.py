'''def decor_uppercase(funct):
    def decor_wrapper(txt):
        return funct(txt.upper())
    return decor_wrapper

@decor_uppercase
def demoUpperDecor(txt):
    print(txt," After decor",txt)

demoUpperDecor("testing")'''
def decor_findmaxnum(func):
    def wrapper(*arg):
        return func(max(arg))
    return wrapper
@decor_findmaxnum
def findMaxNum(*arg):
    print("Maximu number is",*arg)

findMaxNum(1,2,3,4,5)