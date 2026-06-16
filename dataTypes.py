#use of float data dataType look every value in points like 2.5 is a float value
a = 5    # this is A int value or int data Type
b = 2.5  #This is a float data type
c = 5.5
#let's try to declare some complex values
d = 5j
e = 3 + 6j
f = 6j
#g = 5c# this will give you the error bcz we can only represent the complex data type with the j or c or any other latter

print(a + b)  # here I use the addition operator

# let's search ab
# out complex data Type in complex datat Type there this 2 parts one is real and second part is imaginary part like this 3 + 4j or to declare the complex data Type you can also use the complex constructor or complex function

c1 = 3 + 4j # in this variable I store the value 3 + 4j in this part 3 is real number but 4j is imaginary
print(c1)
print(c1.real)
print(c1.imag) # its output will be 4.0 why is that bcz the python only store the values into the points so that is why the result of imaginary is coefficient with float

# remember that python always treat the complex data type in float even if it is real or imaginary part like this 3 = 3.0 and 4j = 4.0j


print("lets print the all the Data types with addition operator")
print(c1.imag + a +b)

print("lets do the same thing with real part")
print(c1.real + b + a)

print("lets print all three data Types with * operator")
print(c1.real*b/2)

print("lets see what will happen if we made every data type others exponential")
print(c1.real**b**a)

print("now lets print all three of them with bitwise operator")
#print(c1.real & a) # the result will be nothing bcz bitwise operators only work with integer data type

print("lets try to add the both floats values ")
print(b + c)

print("lets try to multiply both float values")
print(b * c)

print("lets try to divide the both float values")
print(b / c)

print("lets try to make the both float values each other exponential")
print(b ** c)

print("lets try to comparison both float values")
print(b > c)
print(b < c)

print("now lets try with complex data type and add operators on them")
print(d + e)

print("now lets try to divide the complex data types")
print(d / e)

print("now lets try to use the exponential on complex values")
print(d ** e)

print("now lets try to us the comparison operator on complex values ")
print(d == a)
print(d == e)

# print(d < f)
# print(d > f) these part only cause the error bcz you  can not complex with complex

# print(d > e)
# print(d < e) # comparison operator is not going to work on complex data types

# print(d < a) this is also cause the error bcz the complex and int also cannot be able to compare




#let's try integer data type example
a = 10
b = 20
c = 30
#now lets try to use the operations with integer values
print('lets try to use the +')
print(a + b)

print('lets try to use the -')
print(a - b)

print('lets try to use the *')
print(a * b)

print('lets try to use the /')
print(a / b)

print('lets try to use the /')
print(a ** b)

print('lets try to use the %')
print(a % b)

# now let's try to use store them in variable
print("lets try to use the + operation by storing the values in  ")
sum_ab = a + b
print(sum_ab)

print("lets try to use the - operation by storing the values in  ")
diff_ab = a - b
print(diff_ab)

print("lets try to use the * operation by storing the values in  ")
prod_ab = a * b
print(prod_ab)

print("lets try to use the / operation by storing the values in  ")
dic_ab = a / b
print(dic_ab)

print("lets try to use the % operation by storing the values in  ")
mod_ab = a % b
print(mod_ab)

print("lets try to use the % operation by storing the values in  ")
exp_ab = a ** b
print(exp_ab)


#Let's try the same thing with float
e = 22.5
d = 33.5

print("lets try to use the + operation by storing the float values in  ")
sum_ed = e + d
print(sum_ed)

print("lets try to use the - operation by storing the float values in  ")
diff_ed = e - d
print(diff_ed)

print("lets try to use the * operation by storing the float values in  ")
prod_ed = e * d
print(prod_ed)

print("lets try to use the / operation by storing the float values in  ")
dic_ed = e / d
print(dic_ed)

print("lets try to use the % operation by storing the float values in  ")
mod_ed = e % d
print(mod_ed)


#Let's try the same thing with complex
f = 3j + 3
g = 2 - 3j

print("lets try to use the + operation by storing the complex values in  ")
sum_fg = f + g
print(sum_fg)

print("lets try to use the - operation by storing the complex values in  ")
diff_fg = f - g
print(diff_fg)

print("lets try to use the * operation by storing the complex values in  ")
prod_fg = f * g
print(prod_fg)

print("lets try to use the / operation by storing the complex values in  ")
dic_fg = f / g
print(dic_fg)

# we can also specify the data type
"lets try to specify the int"
x = int(2.4)
y = int(3.5)
print(x)
print(y)

"lets try to specify the float"
float1 = float(2)
float2 = int(3)
print(float1)
print(float2)

print("lets try to specify the complex")
complex1 = complex(2.8) # this will give you the result 2.8 + 0j
complex2 = complex(4.6) # this will give you the result 4.5 + 0j
print(complex1)
print(complex2)

#now let's talk about the strings
print("lets declare a string first")
institute_Name = "technocation"
address = str("new Lalazar street 20")

print(f"school name {institute_Name}") # f allow you to add the values in the string usign curly braces
print(f"adress is {address}")

# now let's use the multiple line string
print("remember multiple line string use triple quotes")
multiString = """ asad
ali
noman 
nadeem
"""
print(multiString)

# now let's try to use the special character like \n and \t \n is Use to take the strint to the next line and \t add the 8 char space
print("Noman \n Noman")
print("Noman \t Noman")