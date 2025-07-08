import random


print(help(random)) # This will print the help documentation for the random module


random.randit(1, 10) 

num1 = 100
num2 = 200
print(random.randint(num1, num2))  # Generates a random integer between num1 and

print(random.randint()) # print a random float number

options = ['rock', 'paper', 'scissors']
print(random.choice(options))  # Randomly selects an element from the list



cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(random.shuffle(cards))  # Shuffles the list in place

