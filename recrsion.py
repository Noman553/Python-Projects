# let's learn what is recursion when a function call itself is called recursion think of it like russian dolls open the big doll  - and you will see a small doll inside of it and when you open that small doll -  you will see another small doll and this process repeats until you reached the last doll that is can not be opened
print("let's learn what is recursion is")
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n -1)

countdown(5)

print("Lets find out the factorial ")
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n -1)
print(factorial(5))

#let's try fibonacci numbers
print("lets try the fibonacci numbers")
def fibonacci_numbers(n):
    if n <= 1:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n - 2)

print(fibonacci_numbers(7))

