#Part A: Find the average of the following numbers:
#ii. 39,45,55,90,95,96
#iii. 54,-45,-10,90
#iv. 55,65,75,95,32

import math

num = [39, 45, 55, 90, 95, 96]
num2 = [54, -45, -10, 90]
num3 = [55, 65, 75, 95, 32]

print(num)
print(num2)
print(num3)


print(f"The average of the first set of numbers is", float(sum(num))/len(num))
print(f"The average of the second set of numbers is", float(sum(num2))/len(num2))
print(f"The average of the third set of numbers is", float(sum(num3))/len(num3))


#Part B: Write a program that tells if the following specific numbers are even or odd.
print("Part B:")
print("Lets now take a look at odd and even number")

first = 9
second = 19
third = 20

if first % 2 == 0:
    print((first), "is an even number")
else:
    print((first), "is an odd number")
if second % 2 == 0:
    print((second), "is an even number")
else:
    print((second), "is an odd number")
if third % 2 == 0:
    print((third), "is an even number")
else:
    print((third), "is an odd number")
