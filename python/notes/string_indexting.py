# string indexing ~ accessing elements of a squence using [] (indexing operator)
#                   [start : end : step]

# example   # how it works/comments

list = 62641489728632863484

print(list[1])   # print the second element of the list
print(list[:5])  # print the first 5 elements of the list
print(list[5:9]) # print the elements from index 5 to 9
print(list[-1])  # print the last element of the list (negative indexing)/(backward indexing))
print(list[7:])  # print the elements from index 7 to the end of the list
print(list[::2]) # print the elements of the list with a step of 2

# example 2

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")  # alternative     print("XXXX-XXXX-XXXX-" + last_digits)
