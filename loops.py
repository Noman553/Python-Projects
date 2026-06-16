#let's try to learn the for loops and use the lists
# for loop is Use to iterating anything in a sequence it will be a List , tuple , string , set , dictionary
# with the help of loop we can iterate each item in a list , tuple and set
fruitList = ['mango' , 'orange' , 'kiwi' , 'cherry']
for fruit in fruitList:
        print(fruit)

# you can also use the range - Range is most widdly use with for loop when you want to print something for a certain number of time
for X in range(6):
    print(X)

A = "hello"
for a in range(6):
    print(A)

#let's use the range to print the list items
rangeList = ["mango" , "banana" , "cherry" , "kiwi"]
for i in range(len(rangeList)):
    print(rangeList[i])

#let's try to learn the while loop - while loop execute The set of statements until the condition is true
#for Example
i = 1
while i <= 6:
    print(i)
    i += 1 # i = i + 1

# what is happening here it will print the statement until The 'i' is lessThen or equal to the 6
#let's try to use the while loop with lists
whileList =   ["mango" , "banana" , "cherry" , "kiwi"]
i = 0
while i < len(whileList):
    print(whileList[i])
    i += 1

whileList2 =   ["mango" , "banana" , "cherry" , "kiwi"]
while i < len(whileList2):
    print(whileList2[i])
    i+=1


#let's try to use the for loop with tuple
loopTuple = ("apple" , "banana" , "cherry" , "kiwi")
for i in loopTuple :
    print(i)

loopTuple2 = (1 , 2, 3, 4, 5)
for i in loopTuple2:
    print(i)

# let's use the range with for loop
rangeTuple = ("apple" , "banana" , "cherry" , "kiwi")
for i in range(len(rangeTuple)):
    print(rangeTuple[i])

# let's try to use the for loop for Tuple
myTuple = ("apple", "banana", "cherry")
for x in myTuple:
  print(x)

print("lets try to use the range ")
rangeTuple = ("apple", "banana", "cherry")
for x in range(len(rangeTuple)):
    print(rangeTuple[x])

#let's try to use the while loop
whileTuple = ("noman" , "ali" , "asad")
i = 0
while i < len(whileTuple):
    print(whileTuple[i])
    i += 1

# let's try to use the for loop in the dictionaries
# while using the for loop in the dictionaries it will return you only the values not the keys for example
print("lets try to use the for loop ")
forDict = {
    "institute Name" : "Technocation",
    "co-founder and ceo " : "sir usman Abid ",
    "students" : 20,
    "location" : "new lalazar cultax road"
}
for x in forDict :
    print(x)

# now you can see that its giving me only the values we can use the values function for the values
print("lets try to print the value() function ")
forValueDict = {
    "Car-brand" : "Honda",
    "model" : 1971 ,
    "color" : "white",
    "suspentions" : True
}
for x in forValueDict.values():
    print(x)

# now lets use the item and if you remember we use the items() function once and it gives us the list and inside the list tuples this items function do the same
print("lets try to print the items function")
itemForDict = {
    "Student Name" : "ALi",
    "Roll No" : 23,
    "Age" : 20,
    "class" : "12th",
    "contact" : 3486120924, # python did not allow us to start the integer with 0

}
for x in itemForDict.items():
    print(x)
