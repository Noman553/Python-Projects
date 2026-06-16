# set can be change OR you can say that the - we can change the sets - but we cannot change the frozen sets
print("lets try to use the frozen sets")
forzenSet1 = frozenset({1 , 2, 3 ,4 })
print(forzenSet1)

#let's try to use the difference did you remember that the difference print those values that are different form the other set
differenceSet = frozenset({1 , 6 ,7 , 8})
differenceSet2 = frozenset({1 , 5 , 9 , 0 , 8})
differenceSet3 = differenceSet.difference(differenceSet2)
print(differenceSet3)

# let's try the intersection remember we once use the intersection And it - Give us those values that are same means work opposite form the difference
intersectionFrozenset = frozenset({1 , 2, 3 , 4, 5})
intersectionFrozenset2 = frozenset({1 , 9, 8 , 6, 5})
intersectionFrozenset3 = intersectionFrozenset.intersection(intersectionFrozenset2)
print(intersectionFrozenset3)

#we also have is isdisjoint() function it give's us result in True or False if there is no intersection between 2 sets it will give us the true if the 2 sets have intersection it will give us False
isdisjointFrozenset = frozenset({"noman" , "ali" , "asad"})
isdisjointFrozenset2 = frozenset({"noman" , "nadeem" , "kami"})
isdisjointFrozenset3 = isdisjointFrozenset.isdisjoint(isdisjointFrozenset2)
print(isdisjointFrozenset3)

# let's try to use the symmetric_difference
a = frozenset({1 , 2, 3} )
b = frozenset({3 , 2 , 5})
c = a.symmetric_difference(b)
print(c)

