# python quiz game

questions = ("how many time zones are in russia?",
             "what is the national flower of japan?",
             "how many stripes are on the US flag?",
             "what is the capital of australia?",
             "what is the largest desert in the world?",)

options = (("A. 11", "B. 4", "C. 10", "D. 9"),
           ("A. cherry blosom/sakura", "B. lilly", "C. dafadil", "D. daisy"),
           ("A. 14", "B. 19", "C. 13", "D. 20"),
           ("A. canberra", "B. sydney", "C. melbourne", "D. paris"),
           ("A. antarctica desert", "B. sahara desert", "C. thar desert", "D. arabian desert"),)

answers = ("A", "A", "C", "A", "A")
guesses = []
score = 0
question_number = 0

print("Welcome to the Quiz Game!")
print("Please answer the following questions by entering A, B, C, or D.\n")
print("====== Questions ======")
for question in questions:
    print("=======================")
    print("Question " + str(question_number + 1) + ": " + question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter A, B, C, or D: ")
    guess = guess.upper()
    guesses.append(guess)
    
    if guess == answers[question_number]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was " + answers[question_number])
    
    question_number += 1
    print("\n")

print("====== Results ======")

print ("Your answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print("Your score is: " + str(score) + "%")





