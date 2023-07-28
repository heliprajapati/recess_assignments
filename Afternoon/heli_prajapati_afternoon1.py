"""Python can be used for Development (using aframework Django),
Machine Learning/Data Science/Artificial Intelligence.
"""
# Running Python Scripts
"""
Multiline comments
"""
print('Running Python Scripts')
print ("I love Python Scripts")

# PEPS: Python Script guidelines
# Indentation 1s
# snake case
#Camelcase This is a camelcase version

#comment
#This is asingle line comment

"""
Multiline comments
"""
#Variables
name="heli"
age="20"
print(name)
print(age)
x,y,z=10,20,30
x,y=25,50
print(x,y)

#Data structures

#Numeric numbers are 1- 10
#integer numbers are int
w=50
print(type(w))

"""
float values are pi=3.14, and 5.1

String values are str
'heli' or "prajapati", Numbers inform of string "10" '5'
example
"""
name = "Heli Praja"
print(name.upper())
print(name)
print(name.lower())
print(name)

#Operators
#Arithmetic Operators
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print( 5 // 2)
print(5 % 2)
print(5 ** 2)
#logical operator
# or -> (atleast one is true)
# and -> (both are true)
# not -> (reverses any value)
#Comparison Operators
#is_greater = 1 > 5
# 1 <= 5
# 1 >= 5
#is_not_equal = 1 != 5
"""
Boolean values are logical values
bool values logical True or False

Sequence types

list - enclosed with square brackets [] and allow duplicate values
They are used to storemany items in a single variable

example
"""
Afternoon = ["HP", "MAC", "DELL","HP","HP","MAC"]
print(Afternoon)
#List length
print(len(Afternoon))
#List Type
print(type(Afternoon))
#Access List items
print(Afternoon[2])
print(Afternoon[-3])
#range
print(Afternoon[3:5])
print(Afternoon[:5])
#Add List items
Afternoon.append("LINUX")
print(Afternoon)
#Add list items using insert method
Afternoon.insert(0,"HPLITE")
print(Afternoon)
#Remove list items
Afternoon.remove("LINUX")
print(Afternoon)
#Remove list items using an index
Afternoon.pop(0)
print(Afternoon)

"""
tuple - enclosed with parenthesis ()
Tuples are used to store items in a single variable
Tuples are immutable

example
"""
phones = ("samsung","iphone","techno")
print(phones)

#Allow for duplicate values
phones=("samsung", "iphone", "techno", "techno", "samsung")
print(phones)

"""
The len() method returns length of the tuple
"""
print(len(phones))

#Tuple with different data types
Tuple1=("matooke","rice")
Tuple2=(100, 200, 300, 500)
print(type(Tuple2))

#how to access tuples
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

#for loop in a 

phones = ("samsung", "iphone", "techno")
for y in phones:
    print(y)


#For iteration
#While Loop
i = 1
while(i <= 5):
    print(i)
    i = i + 1
#For Loop (to iterate over a list)
for i in range(5):
    print(i)
    i = i + 1

"""
Mapping types
Dictionary
dict - dictionary enclosed with curly braces{}
{name: 'heli', age:20}
dict items
{apple, mango, banana}
"""
#example
marks = {"java" : 95, "python" : 98, "php" : 97}
print(marks)
print(marks["python"])

"""
Set types
{apple, mango, banana} unordered collection type, unique
#store multiple items in a single variable
#immutable but one can remove or add items
"""

setone = {"rice", "matooke", "irish"}
print(setone)

#Duplicates in sets is not possible
setone = {"rice", "matooke", "irish", "irish"}
print(setone)

#Exercise find the length of your set, data type, accessing items in a set, add items, add 2 sets together

#length of set
print(len(setone))

#datatypes
#strings
set1={"HP", "DELL"}
#numbers
set2={1, 2, 3, 4}
#tuples
set3={(1, 2), ("a", "b", "c"), (3.14,)}
print(type(set2))

#accessing items in a set
setone = {"rice", "matooke", "irish"}
my_list = list(setone)
print(my_list[1])

#adding items in the set
setone.add("beans")
print(setone)

#add 2 sets together
result = set1 | setone
print(result)

"""
None types: none represents absence of a value
name: none 
"""
gen_gender_sex = True
print(gen_gender_sex)

#If statements
age = 13
if age >= 18:
    print("you are an adult")
elif age < 13:
    print("you are a child")
else:
    print("thank you")

#Taking Input
hobby=input("what are your hobbies ")
print(hobby)




