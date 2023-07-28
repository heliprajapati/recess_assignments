#Tuples
#Tuples are used to store items in a single variable
#Tuples are immutable
phones = ("samsung","iphone","techno")
print(phones)
#Allow for duplicate values
phones=("samsung", "iphone", "techno", "techno", "samsung")
print(phones)
"""

#Exercise use the len() with this tuple example
The len() method returns length of the tuple
"""
print(len(phones))

#Tuple with different data types 
Tuple1=("matooke","rice")
Tuple2=(100, 200, 300, 500)
print(type(Tuple2))
#Exercise how to access tuples
print(phones[-1])
phones = ("samsung", "iphone", "techno")
z = list(phones)
z.append("Nokia")
phones = tuple(z)
print(phones)
#Add two tuples together
laptops = ("Dell","HP", "Acer")
Laptop = ("samsung",)
laptops += Laptop
Newstock = laptops + Laptop
print(laptops)
print(Laptop)
print(Newstock)
#for loop in a tuple
phones = ("samsung", "iphone", "techno")
for y in phones:
    print(y)
