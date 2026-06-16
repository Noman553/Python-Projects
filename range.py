# range are returns the specific sequence of the number it is mostly use fo looping this set of numbers has its own data types
from Scripts.activate_this import existing_pkg_config_path

x = range(10)
print(x)
print(list(x))

#let's try the start and stop arguments
argumentsRange = range(3 , 10)
print(argumentsRange)
print(list(argumentsRange))

# let's try to give a range with step like I want to print the values form 3 to 10 but with after 2 steps like this
stepRange = range(3 , 10 , 2)
print(stepRange)
print(list(stepRange))
# the result will be 3 , 5 , 7 , 9

# let's try to use the slicing ranges like this
sliceRange = range(10)
print(sliceRange[2])# this will only print 2
print(sliceRange[:3]) # it will start from 0 to 3

# let's try to see if the number is - exist or not
existRange = range(0 , 10 )
print(list(existRange))
print(7 in existRange)
print(10 in existRange)
if 10 in existRange :
    print("yes 10 exist")
else:
    print("10 does not exist")

    existRange2 = range(0 , 10 )
if 3 in existRange2 :
    print("yes 3 exist")
else:
    print("3 does not exist")

# let's try to see the length of the range
lenRange = range(0 , 10 , 2)
print(len(lenRange))
