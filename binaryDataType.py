#in bytes data type it convert all the data into the in to 0 and 1 bcz or binary means 0 and 1 and our computer also only understand the language of binary

# first let's try the Byte's
#bytes object store the data in 0 and 1 but its unchange able  like this
# look a bytes is a sequence of number from 0 to 255 that represent the data in binary form

b = b"Hello" # its Convert the string into the ASCII code
print(b)
print(type(b))
#like Upper said that the bytes is not changeable why bcz it bytes did not allow to change or modified it after creating like
# b[0] = 72 this will give you the error

# now let's learn about the array of bytes or bytearray
#A bytearray is similar to bytes but its changeable means we can change it

a = bytearray(b'Hello')
print(a)
print(type(a))
a[0] = 72
c = bytearray(b'Noman')
print(c , "before a")
c[0] = 100
print(c , "after c")
c[2] = 200
print(c , "new c")
c[3] = 100
print(c , "new c")

# Memory view





