#Sets
#store multiple items in a single variable
#immutable but one can remove or add items
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
