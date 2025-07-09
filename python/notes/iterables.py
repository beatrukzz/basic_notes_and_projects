# iterables = An object/collection that can return its elements
#             one at a time, allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" - ")

# tuples are also iterable

names = ("Alice", "Bob", "Charlie")
for name in names:
    print(name, end=" ")

# strings are also iterable

greeting = "Hello"
for char in greeting:
    print(char, end=" - ")

# iteraing sets

fruits = {"apple", "banana", "cherry"}  # cant reverse a set
for fruit in fruits:
    print(fruit, end=" | ")

# iterating dictionaries

my_dictionary = {"A:1", "B:2", "C:3"}
for key in my_dictionary:
    print(key)

for key in my_dictionary.values():
    print(key)

for value in my_dictionary.keys():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
