#Homework 4

#Google how to convert strings from lower to uppercase and upper to lowercase.
#Show your work(screenshot) and add the resources you used.

#string = 'Kalicia Nesbeth'
#string2 = 'kalicia nesbeth'
#print(string.upper())
#print(string.lower())
#print(string.swapcase())
#print(string2.capitalize())

#Write a Python function that takes a number as a parameter and check if the number is prime or not.

def check_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print("Is this a prime number?", check_prime(3))

#########################################################################################################################################
#write a program that takes 5 arguments, checks if each argument is even or odd and returns the number of even and odd numbers/arguments.

numbers = (2, 9, 15, 22, 26) 
num_odd = 0
num_even = 0
for x in numbers:
        if not x % 2:
    	     num_even+=1
        else:
    	     num_odd+=1
print("Number of even numbers :",num_even)
print("Number of odd numbers :",num_odd)
