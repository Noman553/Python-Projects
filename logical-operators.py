# logical operators are Use to add compare two conditions there are 3 types of logical operators and or and not
print("and operator prints the value only if both conditions are true")
a = 10
b = 20
if a > b and b > a :
    print("both condition are true")
else:
    print('one of the condition is not true')

# now let's say that I have two students in a class and I want to see that both are present in the class or not
student1 = "Noman"
student2 = "ALi"
if student1 == "Noman" and student2 == "ALi":
    print("both students are present")

# or operator is Use to combine two condition even if one of the condition is true it will give you the result
#let's say that there is raining Outside and I say if there is not reining outside go out - but then I say even if there is raining outside still go out
print("let's try to use the or operator or operator give us the result even if the one of the condition is true")
is_raining_outSide = False
sky_is_clear = True
the_road_is_closed = False
if is_raining_outSide or sky_is_clear or the_road_is_closed:
    print("go out")

#let's learn about the not operator always reverse the result like sometimes you want that even if the condition is not true print something
a = 33
b = 200
if not a > b:
    print("a is greater then the b")

#let's try multiple conditions
age = 18
is_student = False
has_discount = True
if(age < 18 or age > 65) and not is_student or has_discount:
    print("Every thing is fine")

# remember use the parentheses complex condition
temperature = 25
is_raining = False
is_weekend = False
if(temperature > 25 or not temperature < 25) and is_raining or is_weekend:
    print("greate")

#let's create the login function and see the user is available or not
userName = "Noman55" # remember python treat nonempty string as true
password = "LLogin553@!"
is_verified = True
if userName and password and is_verified:
    print("welcome Back")
else:
    print("login Failed")

print("lets use the empty sting")
userName2 = "" # these are the empty strings means false
password2 = ""
is_verified2 = True
if userName2 and password2 and is_verified2:
    print("welcome")
else:
    print("something went wrong")