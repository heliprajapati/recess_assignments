#Dictionary
print("*****************Dictionary**************************************************************")
#Used to store data values in key:value pairs
#They are ordered, mutable and dont allow duplicates
mydict = {
    "phone":"iphone",
    "model":"iphone15",
    "year":"2023"
}
#print(mydict)
#print(len(mydict))
#print(type(mydict))


#Exercise 1: use values () method to return a list of all values in dictionary
print("*****************Exercise 1 output**************************************************************")

pens = {'ballpen':'black', 'pointpen':'blue'}
pen_list = list(pens.values())
print(pen_list)


#Exercise 2: To check if a key does exist in your dictionary
print("*****************Exercise 2 output**************************************************************")

Phones = { 'price':1000, 'year':2023, 'name':'iphone20'}
print('price' in Phones)
print('name' not in Phones)


#Exercise 3: How to change dictionary items, How to update
print("******************Exercise 3 output*************************************************************")

#How to change dictionary items
marks = {'python': 85, 'php': 72, 'java': 90}
marks['php'] = 80
print(marks)
#How to update
d = { 'dog':'friendly' , 'lion':'wild' , 'parrot':'funny' }
d2= { 'dog':'pet' , 'lion':'wild' , 'tiger':'dangerous' }
d.update(d2)
print(d)


#Exercise 4: How to add dictionary items, How remove Dictionary items
print("*******************Exercise 4 output************************************************************")

#How to add dictionary items
emp = { 'salary':1000, 'age':21, 'name':'heli'}
emp['dept']='sales'
print(emp)
#How remove Dictionary items
fruits={'apple':'red', 'banana':'yellow', 'kiwi':'green'}
del fruits['banana'] #delete the item with banana as its value
print(fruits)

#Exercise 5: How you can loop through a dictionary and how to nest dictionary
print("********************Exercise 5 output***********************************************************")

#how to nest dictionary
Employees={'heli':{'age':21, 'salary':200},
          'Jk':{'age':22, 'salary':300}
          }
#looping through a dictionary
for key in Employees:
    print("Employee", key, ':')
    print('Age:', str(Employees[key]['age']))
    print('Salary:', str(Employees[key]['salary']))


#Strings
print("*****************Strings**************************************************************")
#multiline strings
q="""i am doing BSSE
currently doing recess in python"""
#print(q)

#string as arrays
a="afternoon"
#print(a[1])


#Exercise 1 use the len() function to determine the length of the string
print("*****************Exercise 1 output**************************************************************")

languages="php, java, python"
print(len(languages))


#Exercise 2 give an example of using a for loop in string
print("*****************Exercise 2 output**************************************************************")

str1="python"
for i in str1:
    print(i)


#Exercise 3 give an example of slicing in strings
print("*****************Exercise 3 output**************************************************************")

str2="my name is heli"
str3=str2[11:15]
print(str3)


#how to modify strings
a="afternoon"
#print(a.upper())

#remove white space
b=" after noon   "
#print(b.strip())

#string concatenation
c="afternoon"
d="class"
w = c + d
#print(w)
z = c + " " + d
#print(z)

#Format string
#combining string and number
age=21
name="my name is heli and i am {}"
#print(name.format(age))

print("*****************Boolean**************************************************************")
#Boolean
#These evaluate to a true or false
#print(20 < 10)
r = "heli"
z = 30
#print(bool(r))

#Exercise 1 use a conditional statement to show to use boolean
print("*****************Exercise 1 output**************************************************************")

password_valid = input("enter password")
if password_valid:
    print("login successfully")
else:
    print("Invalid password")











