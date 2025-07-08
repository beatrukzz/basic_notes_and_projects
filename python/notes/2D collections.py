# 2D collections in Python
# 2D collections are collections of collections, such as lists of lists or dictionaries of dictionaries.

# 2D lists
# kind like an excel spreadsheet, where each row is a list and each column is an item in the list


fruits =     ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats =      ["chicken", "beef", "pork"]

groceries = [fruits, vegetables, meats] # 2D list
print(groceries)  # prints the 2D list
print(groceries[0])  # prints the first row (fruits)
print(groceries[1][2])  # prints the third item in the second row
print(groceries[2][0])  # prints the first item in the third row
print(groceries[1][0:2])  # prints the first two items in the second row
print(groceries[0][1:])  # prints all items in the first row except the first item
print(groceries[2][1:3])  # prints the second and third items in the third row

# this works too

groceries = [["apple", "banana", "cherry",],
            ["carrot", "broccoli", "spinach"],
            ["chicken", "beef", "pork"]]


for collection in groceries:
    print(collection)  # prints each row in the 2D list


for collection in groceries:
    for food in collection:
        print(food, end = " ")  # prints each item in each row of the 2D list
    print()


# can make 2D tuples/lists/sets/dictionaries in the same way



