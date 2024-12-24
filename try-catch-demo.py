'''try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
'''
#----open file which is not exist
'''try:
    f=open("demo-txt.txt")
    try:
     f.write("Hello Python")
    except:
     print("Something went wrong while writing")
    finally:
     f.close()
except:
    print("Something went wrong write while opening the file.")
'''
#---------raise an error
'''x=-1

if x<0:
 raise Exception("Numbers cannot be below zero")
'''
#----------Raise TypeError
x="hello"
if not type(x) is int:
    raise TypeError("Only integers allowed ")