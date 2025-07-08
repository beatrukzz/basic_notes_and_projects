#  collections = single "variable" used to store multiple values
#  list = []  ordered, changeable, allow duplicates
#  set = {}  unordered, unchangeable (but ADD/REMOVE OK), no duplicates
#  Tuple = ordered, unchangeable, allow duplicates, faster




# lists


dir()   # dir() shows all the attributes and methods of the current module
print(help(list)) # help() shows the documentation for the specified object
len()  # length of a list

fruits = ['apple', 'banana', 'cherry']
print("apple" in fruits)  # check if "apple" is in the list
# boolean

fruits[2] = 'orange'  # change the value at index 2
print(fruits)

fruits.append('grape')  # add an item to the end of the list

fruits.remove()  # remove an item from the list
fruits.pop()  # remove the last item from the list
fruits.clear()  # remove all items from the list
fruits.sort()  # sort the list in ascending order
fruits.reverse()  # reverse the order of the list

fruits.insert() # insert an item at a specific index
fruits.index()  # find the index of an item in the list
fruits.count()  # count the number of occurrences of an item in the list
fruits.copy()  # create a copy of the list

# set

# can use the same methods as lists, but they are unordered and do not allow duplicates

fruits.dir()  # dir() shows all the attributes and methods of the current module
print(fruits.help()) # help() shows the documentation for the specified object




