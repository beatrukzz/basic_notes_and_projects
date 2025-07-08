# Basic knowledge game

print("************************************************")
print("Basic Knowledge Test")
print("You'll get a score out of 10")
print("************************************************")

# Start game
start_game = input("Shall we begin? (yes/no): ").lower()
if start_game == "yes":
    print("Right answer!")
elif start_game == "no":
    print("That's too bad, we're starting anyways.")

# Choose options
score = 0
choice = input("Pick an option: maths, history, geography: ").lower()

if choice == "maths":
    q1 = int(input("What is 2 + 2? "))
    if q1 == 4:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q2 = int(input("What is 100 times 10? "))
    if q2 == 1000:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q3 = int(input("What is 4 + 4? "))
    if q3 == 8:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q4 = int(input("What is 8 + 8? "))
    if q4 == 16:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q5 = int(input("What is 20 + 9? "))
    if q5 == 29:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    print("Your score is", score)

elif choice == "history":
    q1 = input("When did the First World War start? ")
    if q1 == "1914":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q2 = input("When did the Second World War start? ")
    if q2 == "1939":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q3 = input("What year did the Titanic sink? ")
    if q3 == "1912":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q4 = input("What year did the First World War end? ")
    if q4 == "1918":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q5 = input("What year did the Second World War end? ")
    if q5 == "1945":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    print("Your score is", score)

elif choice == "geography":
    q1 = input("How many continents are there? ")
    if q1 == "7":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q2 = input("What is the capital of France? ").lower()
    if q2 == "paris":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q3 = input("What continent is the UK in? ").lower()
    if q3 == "europe":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q4 = input("Where is the Grand Canyon? ").lower()
    if q4 == "arizona":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    q5 = input("Where is Russia? ").lower()
    if q5 == "europe" or q5 == "asia":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        score -= 1

    print("Your score is", score)

else:
    print("Invalid choice. Please restart the game and pick a valid category.")
