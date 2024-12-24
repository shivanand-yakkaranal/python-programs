try:
    a=20
    b=0
    c=a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("I am in the final block")