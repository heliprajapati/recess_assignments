print("*****************Lists**************************************************************")
#Exercise1 (Lists)
#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["Pj", "jk", "RM", "kim", "jin"]
print(names[1])
#2. Write a python program to change the value of the first item to a new value
names[0] = "Heli"
print(names)
#3. Write a python program to add a sixth item to the list
names.append("suga")
print(names)
#4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print(names) 
#5. Remove the 4th item from the list
del names[3]
print(names)
#6. Use negative indexing to print the last item in your list
last_item = names[-1]
print(last_item)
#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
Brands = ["Ios", "HP", "Dell", "Sumsang", "tecno", "Sony", "Nokia"]
print(Brands[2:5])
#8. Write a list of countries and make a copy of it
countries = ['Kenya', 'Uganda','Tanzania']
newCountries=list(countries)
print(newCountries)
#9. Write a python program to loop through the list of countries
for country in countries :
    print (country)
#10. Write a list of animal names and sort them in both descending and ascending order
animals=['lion','elephant','giraffe','zebra','hippo']
ascending = sorted(animals)#ascending order
descending = sorted(animals, reverse=True)#descending order
print("Ascending order:", ascending)
print("Descending order:", descending)
#11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for animal in animals:
    if 'a' in animal.lower():
        print(animal)
#12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["Praja", "kim", "jeon"]
second_names = ["heli", "jin", "jk"]
full_names = first_names + second_names
print(full_names)


print("*****************Tupless**************************************************************")
#Exercise2 (Tuples)
#1. Write a python program to output your favorite phone brand.
x=["samsung","iphone","tecno","redmi"]
fav = x[1]
print ("My favourite is:", fav)
#2. Use negative indexing to print the 2nd last item in your tuple. 
item = x[-2]
print("The second last item is:", item)
#3. Using the phones list above, write a python program to update “iphone” to “itel”
# Convert the tuple to a list
x_list = list(x)
index = x.index("iphone")
x[index] = "itel"
print(x)
#4. Write a python program to add “Huawei” to your tuple.
# Convert the tuple to a list
x_list = list(x)
x_list.append("Huawei")
x_updated = tuple(x_list)
print(x_updated)
#5. Write a python program to loop through the tuple above.
for item in x:
    print(item)
#6. Write a python program to remove/delete the first item in your tuple.
# Convert the tuple to a list
x_list = list(x)
x_list.pop(0)
x_updated = tuple(x_list)
print(x_updated)
#7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(cities)
#8. Write a python program to unpack your tuple.
phone1, phone2, phone3, phone4 = x
print("Phone 1:", phone1)
print("Phone 2:", phone2)
print("Phone 3:", phone3)
print("Phone 4:", phone4)
#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("2nd City:", cities[1])
print("3rd City:", cities[2])
print("4th City:", cities[3])
#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ["Praja", "kim", "jeon"]
second_names = ["heli", "jin", "jk"]
full_names = first_names + second_names
print(full_names)
#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
print(colors * 3)
#12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print("The number of times 8 appears:", count)


print("*****************Sets**************************************************************")
#Exercise3 (Sets)
#1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["latte", "coke", "coffee"])
print(beverages)
#2. Use the correct method to add 2 more items to the beverages set.
beverages.update(["sprite", "milkshake"])
print(beverages)
#3. Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
#4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)
#5. Write a python program to loop through the set above.
for item in mySet:
    print(item)
#6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {"yellow", "white", "orange"}
myList = ["pink", "red"]
mySet.update(myList)
print(mySet)
#7. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {20}
first_names = {"Heli"}
joined_set = ages.union(first_names)
print(joined_set)


print("*****************Strings**************************************************************")
#Exercise4 (Strings)
#1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
age = 20
name = "Heli"
x = str(age) + name
print(x)
#2. Consider the example below;
#txt = “ Hello, Uganda! ”
#Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
print("String without spaces at the beginning:", txt.lstrip())
print("String without spaces in the middle:", txt.replace(" ", ""))
print("String without spaces at the end:", txt.rstrip())
#3. Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())
#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt2= txt.replace('U', 'V')
print(txt2)
#5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
print(y[1:4])
#6. The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!” Write a python program to correct it.
#We can use '' instead of ""
x = 'All "Data Scientists" are cool!'
print(x)


print("*****************Dictionary**************************************************************")
#Exercise5 (Dictionaries)
#1. Write a python program to print the value of the shoe size. 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])
#2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)
#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)
#4. Write a python program to return a list of all the keys in the dictionary above.
keys = list(Shoes.keys())
print(keys)
#5. Write a python program to return a list of all the values in the dictionary above.
values = list(Shoes.values())
print(values)
#6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("size exists in the dictionary.")
else:
    print("size does not exist in the dictionary.")
#7. Write a python program to loop through the dictionary above.
for key in Shoes:
    value = Shoes[key]
    print("Key:", key)
    print("Value:", value)
    print(",")
#8. Write a python program to remove “color” from the dictionary.
del Shoes["color"]
print(Shoes)
#9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)
#10. Write a dictionary of your choice and make a copy of it.
marks = {'python': 85, 'php': 72, 'java': 90}
#copy
marks2 = marks.copy()
print("Original marks:", marks)
print("Copied marks:", marks2)
#11. Write a python program to show nested dictionaries
Employees={'heli':{'age':21, 'salary':200},
          'Jk':{'age':25, 'salary':300}
          }
print("Age of heli:", Employees['heli']['age'])
print("Salary of Jk:", Employees['Jk']['salary'])
# Modifying
Employees['heli']['age'] = 20
Employees['Jk']['salary'] = 350
print("Updated Employees dictionary:")
print(Employees)




















