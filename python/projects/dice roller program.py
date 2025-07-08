import random

print("********************************")
print("Welcome to the Dice Roller Program")
print("********************************")



dice = ["1", "2", "3", "4", "5", "6"]


roll = input("Do you want to roll the dice? (yes/no): ").lower()

if roll == "yes":
    print("Rolling the dice...")
    result = random.choice(dice)
    print(f"You rolled a {result}!")
else:
    print("Okay, maybe next time!")





