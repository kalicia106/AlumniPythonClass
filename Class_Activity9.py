#Ask the user to enter three numbers and save the numbers in a variable
value1 = int(input("please enter the first number\n"))
value2 = int(input("please enter the scond number\n"))
value3 = int(input("please enter the third number\n"))

#Check to see if the numbers can form a triangle
def theorem(value1,value2,value3):

    if (value1 * value1)+(value2 * value2) == (value3 * value3):
        print("It works.  We have a triangle!\n")
    elif (value2 * value2)+(value3 * value3) == (value1 * value1):
        print("It works.  We have a triangle!\n")
    elif (value1 * value1)+(value3 * value3) == (value2 * value2):
        print("It works.  We have a triangle!\n")
    else:
        print("Sorry, this will not work!")
theorem(value1,value2,value3)
