#write a program that tells if the input is in the range of 6 to 12 or 121 to 151
print("Please guess a number in a range that I'm thinking of?")

Inbetween = int(input("> "))

if (Inbetween >=6) and (Inbetween<=12) or (Inbetween>=121) and (Inbetween<=151):
  print("You have selected a number in the correct range")

else:
  print("You have entered a number in the incorrect range")
