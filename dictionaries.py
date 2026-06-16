# dictionaries Is also like list tuple and set use it is also use to store the collection of data - but it - Use the key pairs it was unordered in before the version 3.7 And it did not allow the duplicates like set
from tuple import constructorTuple

firstDict = {
    "name" : "noman",
    "rollNO": 54,
    "class" : "Data Science"
}
print(firstDict)
# I can also print one key
print(firstDict["name"])

print("Dictionaries did not allow duplicates ")
duplicatesDict = {
    "name" : "noman",
    "name" : "Ali",
    "class" : "data science"
}
print(firstDict)

print("we can also use the len()")
print(len(duplicatesDict))

# we can also use the constructor to create a dictionaries
constructorDict = dict(name = "jhon" ,
                       age = 36 ,
                       country = "pakistan")
print(constructorDict)

# let's learn how to access the items of dictionaries
accessdict = {
    "name": "noman",
    "age": 21,
    "class": "data science"
}
print(accessdict["name"])

# we can also use the get)()
print("lets use the get()")
getDict = accessdict.get("class")
print(getDict)

#we can also use th key() it returns all the keys in the dictionaries
print("lets use the key()")
keyDict = {
    "name": "Ali",
    "age": 22,
    "class": "data science"
}
keyDict2 = keyDict.keys()
print(keyDict2)

# the value() is use to list of all the values in the list
print("lets try to print the values()")
valuesDict = {
    "name" : "mushtange",
    "model" : 1977 ,
    "suspenshion" : True
}
valuesDict2 = valuesDict.values()
print(valuesDict2)

# there is a item() function in dictionaries that which give the result in a list inside a tuple like this [("name" , "noman") , ("age" , 21)] you can see that I have a list and inside of the list I have 2 tuple
itemDict = {
    "institute Name" : "Technocation Training and learning institute",
    "Co- founder and Ceo" : "sir Usman Abid",
    "students" : 20,
    "location" : "New Lalazar cultex raod"
}
itemDict2 = itemDict.items()
print(itemDict2)

# let's try to check if the key value pair is exist
print("lets check if the key value pair is exist or not")
existDict = {
    "institute Name": "Technocation Training and learning institute",
    "Co- founder and Ceo": "sir Usman Abid",
    "students": 20,
    "location": "New Lalazar cultex raod"
}
if "students" in existDict :
    print("yes students key value pair is exist")
else:
    print("we are not able to find any thing like this ")


# let's try to change the items
print("lets try to change the item")
changeDict = {
    "name": "Ali",
    "age": 22,
    "class": "data science"
}
changeDict.update({"name" : "noman"})
print(changeDict)

#let's try to add the item
print("we can also add the item")
addDict = {
    "name": "Ali",
    "age": 22,
    "class": "data science"
}
addDict["height"] = 5.6
print(addDict)

# now let's try to learn how to remove the item form the dictionary
print("we can use the pop() method to remove the item")
removeDict = {
    "name": "Ali",
    "age": 22,
    "class": "data science"
}
removeDict.pop("name")
print(removeDict)

print("lets use the del() it is use to remove the specific key frame")
del removeDict["age"]
print(removeDict)

print("now lets try to use the clear() it is use to empty the dictionary")
removeDict.clear()
print(removeDict)

# let's try to use the copy() and try to copy the dict 1 into dict 2
copyDict = {
    "name" : "noman",
    "age" : 21,
    "class" : "data science"
}
copydict2 = copyDict.copy()
print(copydict2)

# did you remember a loop inside the loop is called the nested loop same there is also a nested dictionaries
familyDict = {
    "child1" : {
        "name" : "ali",
        "age" : 20
    }  ,
    "child2" : {
        "name" : "asad",
        "age" : 23
    },
    "child3" : {
        "name" : "nadeem",
        "age" : 24
    }


}
print(familyDict)






