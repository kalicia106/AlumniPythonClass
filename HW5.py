#Question 1
question1 = int(60 * 42 + 42)

print("How many seconds are there in 42 minutes 42 seconds?\n")
print(question1)

#Question 2
question2 = float(1.61 * 10)

print("How many miles are there in 10 kilometers?\n")
print(question2)

#Question 3
question3 = int(83 - 32 * .5556)

print("How mush is 83 degrees Fahrenheit in degrees celsius?\n")
print(question3)

#Question 4
import math


print("import math library and find the square root of numbers 81, 19, 16, 121 \n")
print("math.sqrt(81) :" , math.sqrt(81))
print("math.sqrt(19) :" , math.sqrt(19))
print("math.sqrt(16) :" , math.sqrt(16))
print("math.sqrt(121) :" , math.sqrt(121))

#Question 5
print("Write a program that returns the area of a circle, r = 9 \n")
import math

def area_of_circle(r):
    """Function that defines an area of a circle"""
    a = 9**2 * math.pi
    return a

print (area_of_circle(1))

#Question 6
from sys import argv

#print("write a boolean function that returns true or false if the letter x is in a string provided by the user")

ring = input("Please type a sentence and I will check if it has the letter x in it \n")
def true_or_false(ring):

    if "x" in ring:
        print("This sentence has the letter x in it \n")

    else:
        print("This sentence does not have the letter x in it \n")
true_or_false(ring)

#Question 7
from sys import argv

#print("Write a boolean function that returns tue or false if any of the letters a, e, i , o, u in a string is provided by the user")

vowels = input("Please type a something and I will check if it has a vowel in it \n")
def true_or_false(vowels):

    if "a" in vowels or "e" in vowels or "i" in vowels or "o" in vowels or "u" in vowels:
        print(" Your entry has a vowel in it. \n")
    else:
        print("Your entry does not have a vowel in it \n")
true_or_false(vowels)

#Question 8
import math

print("What is the volume of a sphere with radius 5? The volume of a sphere with radius r is (4/3)πr3. \n")

pi = 3.1415926535897931
r= 5.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ' ,V)

#Question 9
#print("Write a boolean function that returns true if a given input is divisible by 3 or return false otherwise\n")

print("Enter a number and I will tell you if it is divisible by three!\n")
cubed = int(input())

#define the function
def divisible_by_three(cubed):
    #create a conditional statement for the variable that will be entered by user
    if cubed % 3 == 0:
        return "True, This number is divisible by three!"

    else:
       return "False"
#store the function in a additional variable in order to output the return
t = divisible_by_three(cubed)
print(t)

#Question 10
import datetime

print("Import datetime library and print out today's data and current time\n")
now = datetime.datetime.now()

print(now)
#Question 11
import datetime

print("Using the data time library, print out the current year\n")

print("Current year: %d" % now.year)

#Question 11

print("write a function that counts how  many times the letter a is repeated in a given word (get the word from the user as an input)write code that counts the number of letters in a word provided by the user")

print("Enter a word.  I'll tell you how many times the letter a appears.\n")
words= input()
def count_letters(words):
    print(words.count("a"))

count_letters(words)
