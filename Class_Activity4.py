#write a function that takes 2 arguments and if argument 1 is greater than argument 2, divide the 1st argument by the 2nd, if argument 2 is greater than argument1, multiply argument 1 by 10
#call your function 3 times with different values
#if arg1 is greater than arg2, call the function to print a statement
#if arg2 is greater than arg1, call the function to print a statement

def print_one():
    print("this is  call to function print_one")
def print_two():
    print("this is a call to print_two")
def divideandmultiply(a, b):

    if (a > b):
        print (a/b)
    elif (b > a):
        c = a *10
    else:
        print(both are the same)

divideandmultiply (10, 4)
divideandmultiply (9, 2)
divideandmultiply (110, 3)
