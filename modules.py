# module is like a tool box imagine you are a mechanic you have some tools screwdriver and some others tools so instead of holding all of them you put them in a tool box whenever you a tool just open the tool box and take out the tool you needed modules work same modules are like a file that contain function , variables and other features
# for example I have a module math
from pip._internal.network import download

print("====== lets import the module file that we have created======")
import mymodule
a = mymodule.person1["age"]
print(a)

# you can also name the file whatever you like
print("====== lets import the file as mx name ======")
import mymodule as mx
a1 = mx.person1["name"]
print(a1)

# let's say that you have multiple functions in the mymodule so you want only for this you can do this
print("====== let's import the only one function in  mymodule ======")
from mymodule import person1
a2 = person1["age"]
print(a2)
# let's use the dir() this will print all the variables that are used in module
print("==== now lets use the dir() this will print all the variables in the module ====")
a3 = dir(mymodule)
print(a3)

#let's use some build in modules
print("===== lets use some build in modules =====")

print("=====lets use teh platform module======")
import platform
x = platform.system()
print(x)

# let's use the date module
print("====== date module is use to use the date functions like year , date , time etc =====")
import datetime
x = datetime.datetime.now()
print(x)

print("===== let's print just the year ====")
print(x.year)
# let's create the date object the thing is you create the date object and class you need 3 parameters inside the date class constructor  like year , month , day
print("====== let's use construct the date object =====")
date_construct = datetime.datetime(2026 , 6 , 30)
print(date_construct)

# now let's convert the datetime method into the string formate there is a method called strftime() it converts the datetime into string
print("===== let's display the name of the month ===== ")
print(date_construct.strftime("%B")) # here the %B is Use to print the month name

print("===== if you want to see which week day is today so you can use the %A========")
print(date_construct.strftime("%A"))

print("====== if you want to see which day of the month of the month is today you can use the %d ====")
see_day = datetime.datetime.now()
print(see_day.strftime("%d"))

print("====== if you want to see the name of the month in short version like dec(December) you can use small %b")
print(date_construct.strftime("%b"))




# let's use the random module

# random module is - use when you want to do somthing random imagine you have a box and in this box you have paper chits you close your eyes and pic a random chit similarly the random module works
import random
print("lets use the radiant")
# randint generates the random number between two numbers
number = random.randint(1 , 10)
print(number) # the number will always be different

# now let's use the choice
#let's say that I have a bucket of fruits
bucket = ["Apple" , "Banana" , "Cherry"]
choice = random.choice(bucket)
print(choice)

# now lets use the shuffle
#let's say that I have some numbers
numbers = [1 , 2 ,3 , 4 , 5 , 6]
fruits = ["Apple" , "banana" , "cherry"]
random.shuffle(numbers)
random.shuffle(fruits)
print(numbers)
print(fruits)

# now lets use the random feature in the random module its select the random decimal number between 0 and 1

print(random.random())

# now let's use the uniform feature in random module it generates the random decimal values between two numbers
print(random.uniform(1 , 10))


print("====== math module is use to do the math operations=====")
import math # this is like the toolbox a toolbox that contain math features
# let's use some of the build in function of math module like max min and abs
print("===== min function is use to print the lowest value ======")
min_value = min(10 , 90 , 20)
print(min_value)
print("==== max is use to see the highest value =====")
max_value = max(20 , 40 , 50)
print(max_value)
print("===== the abs() function is use to see the absolute positive value ====")
positive_value = -7.25
print(abs(positive_value))
print("===== in the pow function the second value become the power of first value ====== ")
power_value = pow(4 , 3)
print(power_value)

print("===== if you want to see the square root of the value you can use the sqrt() function for that =======")
print(math.sqrt(25))

print("====== math.ceil() return the value upward to the nearest integer ========")
upward_number = math.ceil(1.6)
print(upward_number)
print("=====math.floor() return the value downward to the nearest value =========")
down_ward = math.floor(3.6)
print(down_ward)

print("if you want to see the value of the pi you can use the pi for that =====")
pi_value = math.pi
print(pi_value)
#and the sqrt is a like a tool inside the toolbox







