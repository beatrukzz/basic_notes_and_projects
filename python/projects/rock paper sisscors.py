# Rock, Paper, Scissors game
print("********************************")
print("Welcome to Rock, Paper, Scissors")
print("********************************")

choice = input("Are you ready? YES or NO").lower()
if choice == "no":
  print("I dont think so ..... try again")
  choice = input("Are you ready? YES or NO").lower()
if choice == "yes":
  print("Great!")
else:
  print("you werent ment to answer with that.....so.....try again")
  choice = input("Are you ready? YES or NO").lower()

print("okay lets start")

import random

computer_choice = random.choice(["rock","paper","scissors"])

user_choice = input("rock,paper,scissors .... SHOOT!").lower()

print(computer_choice)

if user_choice == computer_choice:
  print("we tied..i want a rematch")
  user_choice = input("rock,paper,scissors .... SHOOT!").lower()
  computer_choice = random.choice(["rock","paper","scissors"])
  print(computer_choice)
if user_choice == "rock" and computer_choice == "scissors":
  print("you won?...i dont think so...rematch")
  user_choice = input("rock,paper,scissors .... SHOOT!").lower()
  computer_choice = random.choice(["rock","paper","scissors"])
  print(computer_choice)
if user_choice == "scissors" and computer_choice == "paper":
  print("YAY I won better luck next time")
  print("********************************")
if user_choice == "paper" and computer_choice == "rock":
  print("YAY I won better luck next time")
  print("********************************")
if user_choice == "scissors" and computer_choice == "rock":
  print("you won?...i dont think so...rematch")
  user_choice = input("rock,paper,scissors .... SHOOT!").lower()
  computer_choice = random.choice(["rock","paper","scissors"])
  print(computer_choice)
if user_choice == "paper" and computer_choice == "scissors":
  print("YAY I won better luck next time")
  print("********************************")
if user_choice == "rock" and computer_choice == "paper":
  print("you won?...i dont think so...rematch")
  user_choice = input("rock,paper,scissors .... SHOOT!").lower()
  computer_choice = random.choice(["rock","paper","scissors"])
  print(computer_choice)
if user_choice == "rock" and computer_choice == "scissors":
  print("YAY I won better luck next time")
  print("********************************")
if user_choice!= "rock" and user_choice!= "paper" and user_choice!= "scissors":
  print("thats an illegal move your disqualified")
  print("********************************")
