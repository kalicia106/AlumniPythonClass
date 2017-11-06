
#Exercise 14
from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi there, {user_name}, I'm {script} script.")
print("I'd like to ask you a few questions to get to know you better.")
print(f"Where are you from {user_name}?")
home = input(prompt)

print(f"What is your favorite color {user_name}?")
color = input(prompt)

print(f"What is your favorite food {user_name}")
food = input(prompt)

print(f"What is the last good book that you read?")
book = input(prompt)

print(f"""
Alright, from what I can gather, you are from {home},
your favorite color is {color},
your favorite food is {food} and the last interesting book that you read was {book}.
Thanks for sharing.  Talk to you soon.""" )
