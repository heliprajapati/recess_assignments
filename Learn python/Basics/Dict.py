#Dictionary
#Used to store data values in key:value pairs
#They are ordered, mutable and dont allow duplicates
mydict = {
    "phone":"iphone",
    "model":"iphone15",
    "year":"2023"
}
#print(mydict)
#Length od dictionary
#print(len(mydict))
#Data type
#print(type(mydict))
#Accessing dictonary items 
z=mydict["year"]
#print(z)
y=mydict.get("model")
#print(y)
#print(mydict.keys())

print("*****************Exercise 1 output**************************************************************")
#Exercise 1: use values () method to return a list of all values in dictionary
pens = {'ballpen':'black', 'pointpen':'blue'}
pen_list = list(pens.values())
print(pen_list)


print("*****************Exercise 2 output**************************************************************")
#Exercise 2: To check if a key does exist in your dictionary
Phones = { 'price':1000, 'year':2023, 'name':'iphone20'}
print('price' in Phones)
print('name' not in Phones) 


print("******************Exercise 3 output*************************************************************")
#Exercise 3: How to change dictionary items, How to update
#How to change dictionary items
marks = {'python': 85, 'php': 72, 'java': 90}
marks['php'] = 80
print(marks)
#How to update
d = { 'dog':'friendly' , 'lion':'wild' , 'parrot':'funny' }
d2= { 'dog':'pet' , 'lion':'wild' , 'tiger':'dangerous' }
d.update(d2)
print(d)


print("*******************Exercise 4 output************************************************************")
#Exercise 4: How to add dictionary items, How remove Dictionary items
#How to add dictionary items
emp = { 'salary':1000, 'age':21, 'name':'heli'}
emp['dept']='sales'
print(emp)
#How remove Dictionary items
fruits={'apple':'red', 'banana':'yellow', 'kiwi':'green'}
del fruits['banana'] #delete the item with banana as its value
print(fruits)


print("********************Exercise 5 output***********************************************************")
#Exercise 5: How you can loop through a dictionary and how to nest dictionary
#how to nest dictionary
Employees={'heli':{'age':21, 'salary':200},
          'Jk':{'age':22, 'salary':300}
          }
#looping through a dictionary
for key in Employees:
    print("Employee", key, ':')
    print('Age:', str(Employees[key]['age']))
    print('Salary:', str(Employees[key]['salary'])) 



