import math

def func1():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    try:
        a / 0
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    c = (a*a)//b 
    print(c) 
  
func1()