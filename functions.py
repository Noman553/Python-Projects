# function is a block of code which only runs when it's called
# let's create a function
# def keyword is Use to declare a function
# from http.cookiejar import lwp_cookie_str
# from unittest import result
from list import indexList


# from pip._internal.operations import prepare


def my_function() :
    print("this is my first function")

my_function()

# the advantage of function is that when ever you need to use the same code you just have to call the name of the function
#for example
my_function()
my_function()
my_function()

# let's say that you want to change the Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32)*5/9
print(fahrenheit_to_celsius(70))
print(fahrenheit_to_celsius(75))
print(fahrenheit_to_celsius(80))
# return is Use to return data to the function

# you can add arguments in the function you can add as many arguments
def my_function(fname):
    print(fname + " " + "refsnes")
my_function("email") # this is an arguments
my_function("Tobias") # this is an arguments
my_function("linus") # this is an arguments

def email_function(email):
    print("hello" , email)
email_function("nomanmehmood.me@gmail.com")

# you can also give the default value to the parameter it the function is called without the argument
def friends(name = "Hammad"):
    print("hello" , name)
friends("ALi")
friends("Tobias")
friends()
friends("linus")

# let's take the country example
def country (country = "Pakistan"):
    print("Country Name is " , country)
country("sweden")
country("sweden")
country()
country("sweden")

# you can also send the argument with the key values
def animal_Name(animal , name):
    print("my" + " " + animal , "name is" , name  )
animal_Name(animal="dog" , name= "tommy") # these are the key use to assign the values

# you can also mix the positions and keyword arguments
def mix_function(animal , age ,name):
    print("i have a" , animal)
    print("my" , animal , "name is" , name , "and its age is" ,   age)
mix_function(name = "Tommy" , animal="dog" , age = 10)


#let's use a function list as an arguments
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#let's use the dictionary
def dect_function(person_data):
    print("Name:" , person_data["name"])
    print("age:" , person_data["age"])
personDetails = {"name": "emil" , "age" : 23}
print(personDetails)

# the function can return the values what is the difference between the print and return the thing is print only show you the result on screen but did not save the result but return save the result so you can use it letter for example you got 5 +3 = 8 now return save it in memory you can use this 8 letter like multiplying it with other numbers

def return_function(x , y):
    return x + y
result = return_function(5 , 3)
print(result)

#let's create a function that return a tuple
def tuple_funtion ():
    return (10 , 20)
x, y = tuple_funtion()
print("x:" , x)
print("Y:" , y)

# sometimes you do not know how many arguments you need to pass so for that you can use the args(*) before the parameter when you use the * before the parameter  will receive a tuple of arguments now you can select any result according to your requirement
print("lets use the args")
def args_function(*kids):
    print("the youngest kid is" , kids[0])

args_function("Noman" , "Ali" , "Asad")

# print("lets print with return")
# def returnUse_funtion(x , y):
#     return(x + y)
# result = returnUse_funtion(10 , 20)
# print(result)


#let's try something with args
def arg2_function(*args):
    print("the type of args is" , type(args))
    print("Lets print the first item" , args[0])
    print("Lets print the second item" , args[1])
    print("Lets print All the item" , args)

arg2_function("Noman" , "Ali" , "Asad")

#let's use the for loop and args
print("for loop and args")
def loop_args(greeting , *names):
    for name in names:
        print(greeting , name)
loop_args("Hello" ,"Noman" , "Ali " , "Asad")

# print("lets use the while loop here")
# def while_function(*number):
#     while number > 2:
#         continue
#     print(number)
#     number+=1
# while_function(1 , 2 ,3 , 4 , 5)

# the upper example is wrong bcz the thing is while loop is comparing a tuple with integer it will give me an error bcz comparing tuple with integer is not allowed

#let's try something difficult
print("lets try something difficult")
def difficult_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(difficult_function(1 , 2 , 3))
print(difficult_function(10 , 20 , 30 , 40))
print(difficult_function(100 , 200 , 300))
print(difficult_function(5))


print("lets try a new example")
def difficult_function2(*numbers):
    if len(numbers) == 0:
        print("none")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(difficult_function2(3 , 4 , 5 , 7 ,8 ,9 , 1))

# now let's learn why we use the kwargs ** sometimes you do not know who many keyword arguments you need to pass to a function so for you can use the kwargs** if you use this the parameter will receive a whole dictionary as a keyword
def kwarg_function(**kidName):
    print("the last name is " , kidName["lname"])

kwarg_function(fname = "noman" , lname = "Mehmood")

def kwarg2_function(**kwargsVar):
    print("type is : ", type(kwargsVar))
    print("the name is : ", kwargsVar["name"])
    print("The age is : ", kwargsVar["age"])
kwarg2_function(name = "noman" , age = 21 )

# let's combine args * and kwargs **
def combine_function(title , *args , **kwargs):
    print("the title is" , title)
    print("the names are" , args)
    print("additional details are" , kwargs)

combine_function("user Info" , "Noman" , "ALi" , age = 21 , city = "Rawalpindi")


# now let's learn scope a variable only available indide the region where it was created this is called scop
# there are two types of scop local scope and Global scope
#what is a local scope a variable that is created inside the function - and it is only belongs to the function and can be only called inside the function this is called the local scope
print("lets create the local scope")
def local_function():
    x = 10
    print(x)
local_function()

# you can use the local variable or - you can call it inside the child functions means function inside the function
#for example
print("lets call the local variable inside the child function")
def variable_function():
    x= 300
    def inside_function():
        print(x)
    inside_function()
variable_function()

# remember one thing you can use the variable inside the child functions but if you have created the variable inside the child variable you can't use it inside the parent function
#for example
# print("lets try to create the variable inside the child function and call it inside the parent function")
# def parent_function():
#     print(child_variable)
#     def child_function():
#         child_variable = 300
# parent_function()
# this will give you an error

# global scope is a variable that is available anywhere
print("lets create a global variable")
global_varaible = 300 # this is a global variable
def parent2_function():
    print(global_varaible)
    def child2_function():
        print(global_varaible)
parent2_function()


