# number keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),    # perfect for matrixes of data
           (7, 8, 9),    # 2D tuple
           ("",0,"£"))


for row in num_pad:
    for num in row:
        if num == "":
            print(num, end="  ")
        print()



