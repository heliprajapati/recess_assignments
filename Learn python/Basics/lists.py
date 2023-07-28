#Lists
#They are used to storemany items in a single variable
#Lists are ordered, changeable, allow duplicate values
#Afternoon = ["HP", "MAC", "DELL"]
#print(Afternoon)
#Duplicates in Lists
Afternoon = ["HP", "MAC", "DELL","HP","HP","MAC"]
print(Afternoon)
#List length
print(len(Afternoon))
#List Type
print(type(Afternoon))
#Access List items
print(Afternoon[2])
print(Afternoon[5])
print(Afternoon[-3])
#range
print(Afternoon[3:5])
print(Afternoon[:5])
print(Afternoon[1:])
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
