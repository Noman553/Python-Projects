#let's learn about tuple -
# tuple works same as list but the main difference is that the tuple is unchangeable
from pip._internal.req import constructors

thisTuple = ("apple" , "banana" , "cherry")
print(thisTuple[0])

# let's try - make some changes in the list

# thisTuple[2] = "kiwi"
# print((thisTuple))
# this will give you the error

# the tuple is ordered means that the items in it are not changeable

# tuple also allow duplicates
duplicateTuple = ("apple" , "apple" , "banana" , "banana" , "cherry " , "cherry")
print(duplicateTuple)

#you can also find the length of tuple like this
lengthTuple = ("apple" , "cherry" , "kiwi")
print(len(lengthTuple))

# we can also create a tuple with one item like this
print("lets try to use the tuple with one item")
singleTuple = ("apple" ,) # see the comma if you do not use it  means it's not a tuple
print(type(singleTuple))

print("lets try to print the tuple without using the comma")
singleTuple1 = ("apple")
print(type(singleTuple1)) # it will give you the type string

#tuple also allow us to use the all kind of dataTYPES LIKE LIST
dataTypeTuple1 = ("apple" , "banana" , "cherry" , "kiwi")
dataTypeTuple2 = (1 , 2 , 3 , 4)
dataTypeTuple3 = (False , True , False , True)

print(type(dataTypeTuple1))
print(type(dataTypeTuple2))
print(type(dataTypeTuple3))

print("lets try different datatypes in single tuple")
defDataTypeTuple = ("apple" ,2 , False , "banana" , 10 , True)
print(type(defDataTypeTuple))
print(defDataTypeTuple[0])
print(defDataTypeTuple[3])
print(defDataTypeTuple[2])

# we can also use the tuple constructor like List constructor
constructorTuple = tuple(("apple" , "banana" , "cherry" , "kiwi"))
print(constructorTuple)
#let's see how the access tuple works
# there are different ways to access the tuple
print("we can access the tuple through the indexes")
accessTuple = ("apple" , "banana" , "kiwi" , "melon")
print(accessTuple[0])
print(accessTuple[1])
print(accessTuple[2])

#let's try negative index to access the tuple items
print("we can also access the tuple items with negative indexes")
negativeTupleIndex= ("apple" , "banana" , "kiwi" , "melon")
print(negativeTupleIndex[-1])

#you can specify the range by specifying that where to start and where to end
print("lets try to print the tuple items with range")
rangeTupleIndex= ("apple" , "banana" , "kiwi" , "melon" , "cherry" , "grapes")
print(negativeTupleIndex[2 : 5])

# now let's try the [-1 : -4]
rangeTupleIndex2 = ("apple" , "banana" , "kiwi" , "cherry")
print(rangeTupleIndex[-4 : -1])

# let's try to check the item is Exist in tuple or not
checkTuple = ("apple" , "banana" , "kiwi" , "cherry")
if "apple" in checkTuple:
    print("apple exist" )

# we cannot change the tuple items but the thing is there is way to update the tuple by converting it into the
convertTuple = ("apple" , "banana" , "kiwi" , "cherry")
newList = list(convertTuple)
newList[1] = "kiwi"
print(newList)
# now you are able to use the all the functions like remove() , append() , extend() in your tuple
newList.remove("apple")
print(newList)
newList.append("melon")
print(newList)

#unpacking in tuple the thing is when we create a tuple we normally assign values to it but the thing is we are able - extract all the values back into the variable
print("lets try unpacking")
unPackingTuple = ["apple" , "banana" , "cherry" , "melon"]
(red , yellow , orange , green) = unPackingTuple
print(red)
print(green)
print(yellow)
print(orange)

#remember if you have less - variables then the values you can use the Asterisk *
unPackingTuple2 = ["apple" , "banana" , "cherry" , "melon"]
(red , green , *yellow) = unPackingTuple2
print(red)
print(green)
print(yellow)







