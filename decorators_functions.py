
# think of decorators a toll booth if you want to get the access of next road or city you need to cross the toll booth also think of decorators as A adding new features to a function think of it's like the gift you wrap a gift with the gift wrapping paper now the gift is same - but you have , add a new feature to it
#from unittest import result

print("lets try with out decorators")
def changecase(func):
    def my_inner():
        return func().upper()
    return my_inner()
def my_function():
    return "hello sally"
print(my_function())

# this function result will be only hello Sally with lower case it did not run the upper function bcz we only call the my_function at the last so we will use the decorator
print("let's try with decorator")
def decorator_function(func):
    def inner_decorator():
        return func().upper()
    return inner_decorator
@decorator_function # this is my decorator now the next function well be executed after the decorated_function()

def new_function():
    return "hello sally"
print(new_function())
# it will be like this new_function = decorated_function(new_function)



#now lets use the arguments in decorators
print("lets add the arguments with decorators")
def casechange_functino(func):
    def inner_function(x):
        print("x will receive the value" , x)
        result = func(x)
        print("now the value will return to the original function")
        return result.upper()
    return inner_function
@ casechange_functino
def newcase_fuction(name):
    return "Hello" + name
print(newcase_fuction("jhon"))

# newcase_function = casechange_function(func)

# let's use the *args and **kwargs in decorator example to secure our data
def argsdec_function(func):
    def innerdec_function(x):
        print("receive the values")
        result = func(x)
        print("now return the function")
        return result.upper()
    return innerdec_function

@argsdec_function
def argnew_function(name):
    return "hello" + name

print(argnew_function("jhon"))

# now let's learn what is metadata in python and what is preserving the metadata  is about the information about the function like funtion name function documentation and module name
#for example
def greet():
    """this is greeting function"""
    return "Hello"
print(greet.__name__)
print(greet.__doc__)
# the metadata for this is - greet and this is greeting function

# now what will happen if we use the decorator
print("lets use the decorator")
def changecase(func):
    """this is a greeting function"""
    def inner_function():
        return func().upper()
    return inner_function
@changecase
def greet2():
    return "hello jhon"
print(greet2.__name__)
print(greet2.__doc__)
# now this will give the result the inner function and none bcz the thing is now with the decorator you data change with changecase and changecase function is return the inner_function that is why you are seeing that kind of data

# now if you want to preserve your data Or you want to keep your original data you can use this fucntools.wraps this will preserve your data
import functools
print("lets use teh functools wrap")
def changecase2(func):
    @functools.wraps(func)
    def  myinner_function():
        return func().upper()
    return myinner_function()
def newgreeting_function():
    return "hello Jhon"
print(newgreeting_function.__name__)
print(newgreeting_function.__doc__)
# now this will give you the real or original function







