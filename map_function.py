# what is map function suppose you have a basket of fruits - and you want to wash them all so normally you will do take the apple and wash it take banana and wash it take cherry and wash it means you will wash each fruit one by one like a for loop this but what if you have a fruits washing machine you will but the all the fruits in the washing machine and at once - and it will wash all the fruits for you the washing machine is like a map - map do the same take all the items and do some function on them at once and remember that map always return you the map object you can convert into the list by using the list() function

# let's convert all the fruits into the upper case
fruit = ["apple" , "banana" , "cherry"]
result = map(str.upper , fruit )
print(list(result))
# remember upper only works on strings not on tuples and lists you need that is why on the upper example I apply the upper function on each string for the fruits


