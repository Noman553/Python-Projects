#if and else condition us use to tell the compiler that run a specific line of code only when the  condition is true

#let's use the - a > b as a condition
print("let's use the a > b :- ")
a = 20
b = 30
if a > b :
    print("a is greater then the b ") # remember always add the white spaces in while printing the line if you are using the conditional statements or the loops
else:
    print("a is less then the b")

#let's try to use the - a <b now
print("let's try to use the a < b condition")
if a < b :
    print("a is less then b ")

#let's try to use the == means a == b condition
print("let's try to use the a == b")
if a == b :
    print("a is equal to the b ") # it will print nothing bcz A is not equal to the b

#you can also check that the number is positive or not
print("let's check the number is true or not ")
number = 20
if number > 0:
    print("the number is positive")

print("now let's try to use the negative number ")
number2 = -10
if number2 > 0 :
    print("the number is positive")
else:
    print("the number is negative")

# let's add the multiple print section in if section
print("let's try to add the multiple print sections in if condition")
print("lets say that i have a condition for vote only those person can vote who are older then 18")
age = 20
if age > 18:
    print("you can vote")
    print("you are adult")
    print("congratulations you can now vote")

print("lets see what happen if we use the less then 18")
age2 = 10
if age2 < 18:
    print("you are not eligible")
    print("you are not adult")
    print("we are sorry to say that you are not eligible for the vote")


# you can also use the boolean expression for the condition
print("let's use the boolean for the condition")
is_logged_in = True
if is_logged_in:
    print("welcome back")


#let's say that your first condition is not true but - now you want to use the new condition so here comes the Elif condition
print("let's use the Elif condition")
c = 20
d = 30
if c > d :
    print("c is greater then d")
elif c < d :
    print("c is less then the d")

#let's try to use the multiple conditions
name = "noman"
age = 20
if name == "noman":
    print("Hi Noman")
elif age == 20:
    print("hows you doing")
# it will never run the second condition bcz if condition is already true so the compiler will stop compiling the code first condition

#now let's use the multiple conditions
print("let's say that i have score")
score = 70
if score > 90:
    print("you got highest score")
elif score >80:
    print("you got second highest")
elif score >= 70:
    print("you got 3rd highest")

# let's try with days
days = 3
if days == 1:
    print("Monday")
elif days == 2:
    print("tuesday")
elif days == 3:
    print("wednesday")
elif days == 4:
    print("thursday")
elif days == 5:
    print("Friday")
elif days == 6:
    print("saturday")
elif days == 7:
    print("sunday")

