# the match statement is Use to perform different action based on different condition
# instead of writing many if and else statement you can use the match statement
#for example
day = 4
match day:
    case 1 :
        print("monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednesday")
    case 4 :
        print("thursday")
    case 5 :
        print("friday")
    case 6 :
        print("saturday")
    case 7 :
        print("sunday")

# we can use the underscore for the late code block
day2 =  4
match day:

    case 7 :
        print("saturday")
    case 6 :
        print("sunday")
    case _:
        print("looking forward to weekend")

# you can use the | as a or operator means if you want to compare multiple conditions you can use this like
day3 = 4
match day3 :
    case 1 | 2 | 3 | 4 | 5 | 6:
        print("today is thursday")
    case 5 | 6:
        print("idk")