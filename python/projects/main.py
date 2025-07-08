import math

# calculator
def calculator():
  x = float(input("Enter first number: "))
  y = float(input("Enter second number: "))
  operation = input("Enter operation: ")
  if operation == "+":
    add(x,y)
  elif operation == "-":
    subtract(x,y)
  elif operation == "*":
    multiply(x,y)
  elif operation == "/":
    divide(x,y)
  elif operation == "%":
    remainder(x,y)
  elif operation == "**":
    power(x,y)
  elif operation == "sqrt":
    sqrt(x)
  else:
    print("Invalid operation")
# addition
def add(x,y):
   addition_outcome = x + y
   print(addition_outcome)
   return addition_outcome
#subtraction
def subtract(x,y):
   subtraction_outcome = x - y
   print(subtraction_outcome)
   return subtraction_outcome
#multiplication
def multiply(x,y):
   multiplication_outcome = x * y
   print(multiplication_outcome)
   return multiplication_outcome
#division
def divide(x,y):
   division_outcome = x / y
   print(division_outcome)
   return division_outcome
# remainder of division
def remainder(x,y):
   remainder_outcome = x % y
   print(remainder_outcome)
   return remainder_outcome
# power
def power(x,y):
   power_outcome = pow(x,y)
   print(power_outcome)
   return power_outcome
# square root
def sqrt(x):
   sqrt_outcome = math.sqrt(x)
   print(sqrt_outcome)
   return sqrt_outcome
calculator()

