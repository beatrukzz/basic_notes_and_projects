# dictionary = a collection of {key: value} pairs ordered and unchangebale. No duplicates

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Canada": "Ottawa",}

print(dir(capitals))  # Show all methods and attributes of the dictionary
print(capitals)  # Print the entire dictionary

print(help(capitals))  # Show help information for the dictionary


capitals.get("USA")  # Get the capital of the USA
capitals["USA"]  # Another way to get the capital of the USA

if capitals.get("USA"):
    print("that capital exists")
else:
    print("that capital does not exist")
# Check if a key exists in the dictionary

capitals.update({"Russia": "Moscow"})  # Add a new key-value pair
#                                        or update an existing one
print(capitals)  # Print the updated dictionary


capitals.pop("USA")  # Remove the key-value pair for the USA
print(capitals)  # Print the dictionary after removal

capitals.clear()  # Clear the dictionary
capitals.keys()  # Get all keys in the dictionary
capitals.values()  # Get all values in the dictionary
capitals.items()  # Get all key-value pairs in the dictionary

for key in capitals.keys():
    print(key)  # Print each key in the dictionary

values = capitals.values()  # Get all values in the dictionary
for value in values:
    print(value)  # Print each value in the dictionary

items = capitals.items()  # Get all key-value pairs in the dictionary
for item in items:
    print(item)  # Print each key-value pair in the dictionary

# resembles a 2d list of tuples/2d array

#items = capitals.items()  # Get all key-value pairs in the dictionary
for key, value in capitals.items():
    print(f"{key}: {value}")  # Print each key-value pair in the dictionary

# advance topic










