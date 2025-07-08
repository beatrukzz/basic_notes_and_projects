# keyword arguments - an argument preceded by an identifier
#                     helps with readability
#                     order of arguments deosnt matter
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", first="John", last="Doe")  # positional arguments

# positional arguments follow keyword arguments

print("1","2", "3", sep=":", end="\n\n")  # sep is a keyword argument

















