#   for loops = excecutea block of code a fix number of times
#               you can iterate over a range, string, sequence ect


for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):    # reversed/backwords
    print(x)

for x in range(1,11,2):     # the third number is the step (eg counting by 2)
    print(x)

# example
numbers ="345678"
for x in numbers:
    print(x)

for x in range(5):
  if x == 3:      # skips the number 3
      continue    # break would stop the loop
  else:           
      print(x)    # prints 0,1,2,4

for x in range (2,10):
    if x == 4:    # stops the loop at 4
        break
    else:
        print(x)
