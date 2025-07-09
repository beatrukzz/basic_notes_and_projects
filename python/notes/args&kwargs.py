#           *args    = allows you to pass multiple non-key argument
#           **kwargs = allows you to pass multiple keyword-arguments
#                      * unpacking operator
#                      1. positional   2. default  3. keyword  4.ARBITRARY

def add(a,b):
    return a + b
print(add(1,2))



# example of how to use *args
def add_all(*args):   # by using *args we can pass any and however many numbers
    return sum(args)

print(add_all(1,2,3,4,5))  # 15
print(add_all(1,2))        # 3
print(add_all(1,2,3))      # 6


def add(*args):   # *arg can be changed to any name aslong as theres an asterisk in front
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))  # 6
print(add(1,2,3,4,5))  # 15
print(add(10,20))  # 30

def display_names(*names):
    for name in names:
        print(name, end=' ')

display_names('Alice', 'Bob', 'Charlie')

# example of how to use **kwargs

#def print_adress(**kwargs):
    #print(type(kwargs))  # <class 'dict'>  # kwargs is a dictionary
    #for value in kwargs.values():
        #print(value, end=' ')
    #print()
    #for key, value in kwargs.items():
        #print(f"{key}: {value}")
#print_adress(street='123 Main St', city='New York', state='NY', zip='10001')



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    for key, value in kwargs.items():   # alterantive : print(f"{kwargs.get('key (e.g street))})
        print(f"{key}: {value}")                        #print(f"{kwargs.get('city')}")} {kkwargs.get('state)}  ... so on
#                                                             ~ the word inside the single quaotes('') is the keyword that itll look/print out                                                    
shipping_label('Alice', '123 Main St', city='New York', state='NY', zip='10001')


# **kwargs can be used to pass a dictionary as keyword arguments
# **kwargs can also be used in if statements eg:
if "city" in kwargs:    # has to be inside a function to work
    print("City is present in kwargs")
else:
    print("City is not present in kwargs")
 
shipping_label('Alice', '123 Main St', city='New York', state='NY', zip='10001')

