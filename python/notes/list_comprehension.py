# list comprehenstions = Aconsice way to create lists in pyhton
#                        Compact and easier to read than traditional loops
#              formula ~ [expressions for value in iterable if condition]

# example of traditional loops

doubles = []
for x in range(1,11):
    doubles.append(x * 2)
    
print(doubles)

# example of list comprehensions

doubles = [x * 2 for x in range(1, 11)]
tripples = [x * 3 for x in range(1, 11)]
squares = [x * x for x in range(1, 11)]
print(squares)
print(doubles)
print(tripples)

# examples with strings

fruits = ['apple', 'banana', 'cherry', 'date']
fruit = [fruit.upper() for fruit in fruits]
print(fruit)


fruit = ['apple', 'banana', 'cherry', 'date']
fruit_charts = [fruit[0] for fruit in fruits]
print(fruit_charts)

# examples with conditionals

numbers = [-1, 2, -3, 4, -5, 6]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(even_numbers)
print(odd_numbers)
print(positive_numbers)
print(negative_numbers)

# examples with nested loops

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)    

# example

grades = [85, 90, 78, 92, 88]
passing_grades = [grade for grade in grades if grade >= 80]
print(passing_grades)
