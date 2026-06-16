#what is the use of set in phyton set is one of the 4 data types that are Use to store collection of data with different qualities like list is ordered and changeable And it also - allow duplicates and 2 - Tuple is also ordered but unchangeable and it also - allow duplicates now set is unchangeable unordered and unindexed

print("lets create a set remember set is created with {}")
firstSet = {"apple" , "banana" , "cherry"}
print(firstSet) # the set is unordered means that every time you use the set the order will change

#the thing is in set if you use the boolean value like True or False it refer as 1 and 0 so if you use True and False and on the same time you also use the 1 and 0 so the compiler will think they are duplicates and since the duplicates are not allowed so it will remove the duplicates like this
print("lets try the different Data types in single set")
set2 = {"apple" , "Islamabad" , True , False , 1 , 0 , 2.5 } # it will remove 1 and 0 bcz compiler thinks that both of them are duplicates
print(set2)

#we use len() length function to see how many items a set contain
print("lets try to use the len function ")
lenSet = {"apple" , "banana" , "cherry" , "kiwi"}
print(len(lenSet))

# we can also use the set constructor to create the set
print("lets use the constructor to create the set")
constructorSet = set(("apple" , "cherry" , "kiwi" , "melon"))
print(constructorSet)

# we can access the items in set by referring the index or key
print("lets try to access the items")
accessSet = {"apple" , "banana" , 3 , 5 , True }
for x in accessSet:
    print(x)

print("lets see if the item is exist in the set")
accessSet2 = {"apple" , "banana" , 3 , 5 , True }
print("apple" in accessSet2)

print("we can also use this method to see that the item exist or not")
accessSet2 = {"apple" , "banana" , 3 , 5 , True }
if "apple" in accessSet2 :
    print("apple exist")
else:
    print("not found")


# in the set add() function us use to add new items the thing is set did not allow you - change item after creating it - but we are able to add the new item
print("lets add new item")
addSet = {"apple" , "banana" , 3 , 5 , True }
addSet.add("cherry")
print(addSet)

# remember we use the extend() to add the item from the previous list to the current list we can do the same thing in set but we use update() function for this purpose
print("lets try to print the items")
updateSet = {"apple" , "banana" , 3 , 5 , True }
newSet = {"Islamabad" , "Gujranwala" , "phalia" , "Malakwal"}
newSet.update(updateSet)
print(newSet)

print("we can also add the lists")
updateSet2 = {"apple" , "banana" , 3 , 5 , True }
myList = ["Islamabad" , "Mandi" , "Gujranwala"]
updateSet2.update(myList)
print(updateSet2)

# we can remove the items form the set the thing is we lean that the set is unchangeable means we are not able to change the set items so how is it possible to remove the items from the set the reason is that we can are not able to change the items by indexes like this
# myset = {"apple" , "banana" , 3 , 5 , True }
# myset[0] = "cherry"
# this will give you the error - but you can use this

print("lets try to remove the item")
removeSet = {"apple" , "Islamabad" , "Cherry" , "Gujranwala"}
removeSet.remove("apple")
print(removeSet)

print("we can also use the discard()")
removeSet.discard("Islamabad")
print(removeSet)

print("we can use the pop() to remove the random item")
removeSet.pop()
print(removeSet)

print("we can use teh clear() to empties the set ")
removeSet.clear()
print(removeSet)

print("we can use the del() to delete the set completely ")
# del removeSet
# print(removeSet)
# this will give you error that the set is not defined

#let's learn about the join the set
print("lets use the union() to join the sets")
unionSet1 = {"apple" , "banana" , "cherry" , "kiwi"}
unionSet2 = {1 , 3 , 6 , 7, 8}
unionSet3 = {True , False}
unionSet4 = {2.5 , 5.5 , 6.6 , 7.7}
unionSet5 = unionSet1.union(unionSet2)
print(unionSet5)

print("we can also use the | instead of the union()")
unionSet6 = unionSet1 | unionSet2
print(unionSet6)

print("we can also join the multiple sets")
unionSet7 =  unionSet1.union(unionSet2 , unionSet3 , unionSet4)
print(unionSet7)

# If - want to only print the duplicates in 2 sets we can use the intersection()
print("lets try to use the intersection")
intersectionSet1 = {"apple" , "banana" , "cherry" , "kiwi"}
intersectionSet2 = {"apple" , "banana" , "melon" , "orange"}
intersectionSet3 = intersectionSet1.intersection(intersectionSet2)
print(intersectionSet3)

print("we can also use the & operator instead of intersection()")
intersectionSet3 = intersectionSet1 & intersectionSet2
print(intersectionSet3)

# we can use the difference() it will only those items that are only in first set not in second set
difSet1 = {"apple" , "banana" , "cherry" , "kiwi"}
difSet2 = {"apple" , "banana" , "melon" , "orange"}
difSet3 = difSet1.difference(difSet2)
print(difSet3)

print("we can also use the - operator instead of difference()")
difSet3 = difSet1 - difSet2
print(difSet3)

# let's see the use of difference_update() its work same as differenc means that it will only print those items that or not available in second list
difSet1.difference_update(difSet2)
print(difSet3)

# we also have A symmetric_difference() this print the items that or not in both sets means only items that are not the same
print("lets try to use the symmetric_difference")
symmetricSet1 = {"apple" , "banana" , "cherry" , "kiwi"}
symmetricSet2 = {"apple" , "banana" , "melon" , "orange"}
symmetricSet3 = symmetricSet1.symmetric_difference(symmetricSet2)
print(symmetricSet3)

print("we can also use the ^ operator instead of symmetric_difference() but the main difference is you cannot be able join the dataTypes like symmetric_difference")
symmetricSet4 = symmetricSet1^symmetricSet2
print(symmetricSet4)







