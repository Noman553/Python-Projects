# string data type is a data type where data is store in double and single quotation marks
a = "hello" # this is a string
print(a)
# you can use the triple double quotes for the multiple line string
a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""

# remember that strings are array in python so you can use the indexes to print a single char
#for example
string_index = "Hello"
print(string_index[1])

# you can loop through the stings bcz the strings are array in python
print("lets try to use the loop on the string")
loop_string = "Noman"
for x in loop_string:
    print(x)

# we use the len() function to get the length of the string
print("lets use the length function to the string ")
length_string = "noman"
print(len(length_string))

# we can also check that the certain character are present in the string or not
char_pre_string = "Lets Check the character is present the string or not "
print(char_pre_string)
print("present" in char_pre_string) # this will give you the true

# you can also use the if statement to see the character is present in string or not
char_pre_string2 = "Lets Check the character is present the string or not "
if "string" in char_pre_string2:
    print("yse the string character is present in the string data type")

# we can use the slicing to get the small part of the string think of it like a cake and taking small part or a slice form the cake
print("let's use the slicing")
slicing_string = "Hello , world"
print(slicing_string[2 : 5]) # remember the first is the starting point and the last is A ending point and  5 is not included

print("let use only the last value in slicing")
print(slicing_string[:5])# now the default first value is 0

print("now let's use the only first value")
print(slicing_string[2 :]) # now the default end point is last character of the string

# let's tyr to use the negative slicing in the string
print("let's use the negative slicing ")
negative_slicing_string = "Hello World"
print(negative_slicing_string[-5 : -2]) # the thing is slicing only work from left to right now look in this example it will start from the -5 and end to -2

#let's modify the string
print("we can also modify the string")

# we use different build in functions to modify the strings
#for example
print("let's use the uppercase() to modify the string")
upperCase_string = "hello world" # here all the char are in lowerCase
print(upperCase_string.upper()) # upperCase() use to convert the lowerCases into the upperCase

# you can use the lower case to convert the upperCases into the lower cases
print("let's use the lowercase() to modify the string")
lowerCase_string = "HELLO WORLD"
print(lowerCase_string.lower())

# you can also replace the word in a string
# for example
print("let's try to replace the string char")
replace_string = "Hello , World"
print(replace_string.replace("H" , "j"))

# we can split the string char where all the string characters become the part of the list
# for example
print("let's use the split() to split the string ")
split_string = "hello, world!"
print(split_string.split(" , "))

# let's lean the concatenation

# the concatenation is combining 2 strings And you can combine two strings with + operator
print("let's concatenate the strings")
a = "hello"
b = "world"
print(a + b)

# remember the thing is you can't combine to different datatype with strings means you can't combine the int datatype with string datatype - but you can use the f string to combine
print("lets use the f string or formate() string")
age = 20 # this is A integer and I want to combine it - so I will use the f string
f_string = f"My name is Noman and my {age}"
print(f_string)

# we also use the placeholders in the f string placeholder are like locations that hold the positions where the variable is going to place
print("lets see what is placeHolders")
age = 20 # this is A integer and I want to combine it - so I will use the f string
PlaceHolder_string = f"My name is Noman and my {age}" # the age is a placeholder
print(replace_string)

# we also have modifiers - modifiers control that how the value inside the placeHolder is going to be shown
print("let's see what is modifiers")
price = 49.999
print(f"this is a modifier : {price:.2f}") # 2f means show 2 values after the decimal numbers
price2 = 50.0000
print(f"lets see what happens now : {price2:.3f}")







