# nested loop  = A loop within another loop (outer,inner)
#                outer loop:
#                    inner loop:


for x in range(3):    # outer loop ~ everything inside this loop will be executed 3 times for example
    for y in range(1,5):
      print(y,end="") # alternative to print(x,end="") is print(x,end="\n") or print(x,end=" ")
                      # end="" is used to print the output in the same line

# alternative version
for x in range(3):    
    for y in range(1,5):
      print(y,end="")
    print()            # this will print the output in the next line (eg 1234\n1234\n1234\n)
                        # this is the same as print(x,end="\n")

# example
rows = int(input("Enter number of rows: "))
coloums = int(input("Enter number of coloums: "))
symbol = input("Enter symbol: ")
for x in range(rows):    
    for y in range(coloums):
      print(symbol,end="")
    print()
