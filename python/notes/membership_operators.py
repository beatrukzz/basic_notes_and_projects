# Membership operators = used to test wether a value or variable is found in a sequence
#                        (string, list, tuple, set, dictionary)
#                        1. in
#                        2. not in
 

# example with a string
word = "APPLE"

letter = input("Enter a letter: ")

if letter in word:                          # alternative if letter not in word:
    print(f"{letter} is in {word}")         # then switch the statements to make sense
else:
    print(f"{letter} is not in {word}")

# 2nd example with a set
names = {"Alice", "Bob", "Charlie"}
name = input("Enter a name: ")
if name in names:
    print(f"{name} is in the set of names")
else:
    print(f"{name} is not in the set of names")

# 3rd example with a list
fruits = ["apple", "banana", "cherry"]
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print(f"{fruit} is in the list of fruits")
else:
    print(f"{fruit} is not in the list of fruits")  

# 4th example with a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
key = input("Enter a key: ")
if key in person:
    print(f"{key} is a key in the dictionary")
else:
    print(f"{key} is not a key in the dictionary")  

# 5th example with a tuple
colors = ("red", "green", "blue")
color = input("Enter a color: ")
if color in colors:
    print(f"{color} is in the tuple of colors")
else:
    print(f"{color} is not in the tuple of colors") 

# 6th example with a range
numbers = range(1, 11)  # range from 1 to 10
number = int(input("Enter a number between 1 and 10: "))
if number in numbers:
    print(f"{number} is in the range of numbers")
else:
    print(f"{number} is not in the range of numbers")       

# 7th example with a string and a for loop
sentence = "Hello, world!"
for char in sentence:
    if char in "aeiouAEIOU":  # check if the character is a vowel
        print(f"{char} is a vowel")
    else:
        print(f"{char} is not a vowel") 

# 8th example with a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers if n in range(1, 6)]
print(f"Squared numbers: {squared_numbers}")

# another example with dictionaries

grades = {"John": "B", "Alice": "A", "Bob": "A"}

student = input("Enter a student's name: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not in the grade book")

# another example with string

email = "beatrukzzx123@gmail.com"

if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")
