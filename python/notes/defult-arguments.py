# defult arguments - A defult value for certain parameters
#                    defult is used when that argument is omitted
#                    make your functions more flexible, reduces no. of functions
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitary



# example 1
def net_price(list_price, discount, tax):
    return list_price*(1 - discount) * (1 + tax)

print(net_price(100, 0.1, 0.2))  # 108.0


# example 2
def net_price(list_price, discount=0.1, tax=0.2):  #(default)assigned values
    return list_price*(1 - discount) * (1 + tax)    
print(net_price(100))  # 108.0
print(net_price(100, 0.2))  # 96.0
# will take in new value inputed instead of default value
# tax will still be 0.2

# full example

import time
import sys

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
        print("\033[F", end="")
    print("done")
        
count(30,15)  # start at 15, end at 30















