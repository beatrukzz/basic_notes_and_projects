# Madlips game

options = input("would you like to play option 1 or 2 of the madlips game?")
if options == "1":
    import random

    adjectives = ["expensive", "cheap", "lovely", "marvelous", "small"] 
    verbs = ["crying", "shouting", "arguing with me"]
    nouns = ["shoes", "dress", "jeans"]

    chosen_adjective = random.choice(adjectives)
    chosen_noun = random.choice(nouns)
    chosen_verb = random.choice(verbs)

    print(f"Today I went to the shops and bought myself a {chosen_adjective} {chosen_noun} but when I went to pay for the   {chosen_noun} my mum started {chosen_verb}, which made me not want to buy the {chosen_noun} anymore and then I went back home")
if options == "2":
  adjectives2 = input("Enter an adjective: ")
  verbs2 = input("Enter a verb: ")
  nouns2 = input("Enter a noun: ")
  print(f"Today I went to the shops and bought myself a {adjectives2} {nouns2} but when I went to pay for the {nouns2} my mum started {verbs2}, which made me not want to buy the {nouns2} anymore and then I went back home")
else:
  print("Invalid option, please choose either 1 or 2")



