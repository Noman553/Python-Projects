# in Python list is Use to store the multiple items in a single variable like this
myList = ['mango' , 'orange' , 'banana' , 'Apple']
print(myList)
# list items are ordered And we can not change them like if you add a new item in the list it will Automatically add to end of the list

# list is also change able means we can add and remove the item from it after it has been created
# Remember that we can not be able to change the list order But we can add and remove the items from the list


#list allow us to add duplicate like this
myList1 = ['mango' , 'Apple' , 'mango' , 'Apple'] # it Happened bcz every item in list has different index
print(myList1)

print("lets check list length")
print(len(myList))

print("lets check list data type")
print(type(myList))

# Remember in list you can add any data type like his
myList2 = ["mango"  , 2 , 3 ,4 , False , True]

# you can also use the list constructor to build the list like this
thisList = list(('mango' , 'orange' , 'Apple'))
print(thisList)

# every item in the list has its own index number And we will be able to print any item in list through the index
print("lets print the list  with index")
indexList = ['Ali' , 'Asad' , 'Noman' , 'Nadeem' , 'Awais' ]
print(indexList[1])

print("lets print the list item throught the negative items")
print(indexList[-1])
print(indexList[-2])

# now lets try to learn the range of index
rangeList = ['Orange' , 'kiwi' , 'Apple' , 'melon' , 'banana']
print(rangeList[2 : 4])
print(rangeList[-1 : -4])
print(rangeList[-1 : -3])
print(rangeList[-3 : -1])

rangeList2 = ['Faisalabad' , 'Multan' , 'Sindh' , 'Karachi' , 'Islamabad' , 'Gujranwala' , 'Mandi-Bhau-din' , 'Malakwal' , 'Phalia' ]
print(rangeList2[-1:-4]) # the result will be nothing OR you can say that it will give you only empty brackets bcz in python list work form left to right and -1 is already on the end of the right so it can not continue
print(rangeList2[-4:-1])

#you can also check if the item is Exist in the list or not
existList = ['Faisalabad' , 'Multan' , 'Sindh' , 'Karachi' , 'Islamabad']
if 'Islamabad' in existList:
        print("Islamabad exist in the existList")

#let's try to insert the item on specific index
insertItems =  ['Faisalabad' , 'Multan' , 'Sindh' , 'Karachi' , 'Islamabad']
insertItems.insert(2 , "indus")
print(insertItems)
insertItems2 =  ['Faisalabad' , 'Multan' , 'Sindh' , 'Karachi' , 'Islamabad']
insertItems2.insert(3 , "indus 2")
print(insertItems2)

# let's learn to append the items
print("lets try to append the items")
appendList = ["orange" , "banana" , "cherry" , "kiwi" ]
appendList.append("melon")
print(appendList)

newFruit = "melon"
appendList.append(newFruit)
print(appendList)


#you will see the suggestion form you code editor which is Multi-step list initialization can be replaced with a list literals why bcz you do not need to use The Append to add a new item in list bcz it do not make sense
# for example

appendList2 = []
appendList2.append("noman")
appendList2.append("ALi")
appendList2.append("Asad")
print(appendList2)
# this make sense

# we use expend() to add the items form the other list to the current list like this
firstList = ["orange" , "banana" , "cherry" , "kiwi" ]
expandList = ['Faisalabad' , 'Multan' , 'Sindh' , 'Karachi' , 'Islamabad']
firstList.extend(expandList)
print(firstList)

#let,s try to use the remove items method form the list
removeList = ["orange" , "banana" , "cherry" , "kiwi" ]
removeList.remove("cherry")
print(removeList)
#let's say that you have double items in your lists like this
removeList2 = ["orange" , "banana" , "cherry" , "kiwi" , "cherry" ]
removeList2.remove("cherry")
print(removeList2)
#here you have 2 cherry in your code so it will automatically remove the first cherry

# if you want to remove the specific index so you need to use the pop() like this
popList =  ["orange" , "banana" , "cherry" , "kiwi" , "cherry" ]
popList.pop(3)
print(popList)

# the del keyword is also use to remove the specific items like this
delList =  ["orange" , "banana" , "cherry" , "kiwi" , "cherry" ]
del delList[3]
print(delList)


# let's learn about list comprehension is a shortcut way to write a new list instead of writing many lines of code with for loop you can use the comprehension and create a list with in one line of code
#for example
numbers = [i for i in range(5)]
print(numbers)

comprehensionList = [ i*2 for i in range(5) ]
print(comprehensionList)

#let's try to do the same thing with for loop
number = []
for i in range(5):
        number.append(i)
        print(number)

#let's try to use the if statement in the comprehension and let's see what will happen
comprehensionList2 = ["apple" , "banana" , "kiwi" , "cherry " , "melon"]
newList = [x for x in comprehensionList2 if x != "apple"]
print(newList)

# first x say that what do I store and for x is a variable of loop on each loop every value will store in it and I have also ADD  the condition which is if x != "apple" now what will it do it will check my comprehensionList and see that my first character is "apple" and store it in the loop x now it will check the condition and the condition is false bcz right now x contain "apple" and my fist character in my comprehensionList is also A "apple" so now condition is false And it is not going to store the value or result in fist x and on second time it will again the  second character in my Original list which is "banana" and it is not equal to "apple" so it means that the condition is true And now it will save the result in first x and add it into the new list

# let's try some of the sorting alphanumerically,
print("lets try to sort the data alphanumerically,")
sortList = [ "banana" , "kiwi" , "cherry", "apple "  , "melon"]
sortList.sort()
print(sortList)

#look how sort works on alphabets our computer only understand 0 and 1 so the question is how alphabets are sort in the thing is every alphabet contain the ascii code(American standard code information interchange) so it compares the ascii codes of alphabets for example I have "apple" and "banana" the ascii code of 'a' is 97 and for 'b' is 98 now 97 is smaller - Then the 98 so first item will be 'apple'

print("lets try to sort numerical values")
numericList = [50 , 20 , 10 , 40 , 90]
numericList.sort()
print(numericList)

# the numerical values does not need to convert into the ASCII code bcz they can be compared directly
print("now lets try to use the reverse method or descending order in sorting")
descendingList = ["apple" , "banana" , "kiwi" , "cherry" , "melon"]
descendingList.sort(reverse=True)
print(descendingList)
# now what will happen here it will start from the bigger to smaller

# let's learn how to copy the list
# for example
copyList = ["apple" , "banana" , "cherry"]
newCopyList = list(copyList)
print(newCopyList)

print("we can also copy this list with slice operator")
copyList2 = ["apple" , "banana" , "cherry" , "melon"]
newCopyList2 = copyList2[:]
print(newCopyList2)

#let's try to learn the joining list
List = [1 , 2 , 3 , 4]
joinList = ['Noman' , 'asad', 'ali' ]
print(List + joinList)

print("lets try to join the list with append")
appendList1 = ["a" , "b" , "c" , "d"]
appendList2 = [1 , 2 , 3 , 4]
for X in appendList2:
        appendList1.append(X)
        print(appendList1)

# we can also use the extend() to join the lists remember extend() is use to add elements from one list to another
extendList1 = ['apple' , 'banana' , 'cherry' , 'melon']
extendList2 = [1 , 2 , 3.55 , 6.6 ,7]
extendList1.extend(extendList2)
print(extendList1)

#list data can be changed so use the list when You know that the data need to be changed like shopping cart












