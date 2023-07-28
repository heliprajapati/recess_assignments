#Functions
#group of blocks of code
#def function_name ():

#Arguments and parameters
def afternoon(first_name,last_name):
    print(f"hi {first_name} {last_name}")
    print("Attendees are close to 100")
#calling function
afternoon("heli","prajapati")

#Modules
#simple calculator
def add(s,w):
    return(s + w)
def multiply(s, w):
    return (s * w)
def subtract(s, w):
    return s - w
import modules
print(modules.multiply(8,4))

from math import *
print(sqrt(25))    
print(cos(pi/2)) 

#Example of taking input from user
"""
number = int(input("enter a value: "))
product = number * 10
print(product)
"""

#Example of multiple inputs
"""
s,r,w = map(int, input("Enter the values : ").split())
print("The values are : ", end = " ")
print(s,r,w)
"""

#How to capture input from tuple
"""
w = (2,4,6,8)
print("current tuple")
print(w)
E = list(w)
E.append(int(input("Enter new value: ")))
w = tuple(E)
print("New Tuple after adding element is")
print(w)
"""

"""
mylist = list(map(int, input("Enter list values : ").split()))
myset = set(map(int, input("Enter set values : ").split()))
print(mylist)
print(myset)
"""

def get_info():
    name = input("Enter your name: ")
    return name
user_name = get_info()
print("Name :", user_name)























