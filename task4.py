""" [[2, 5, 9],
    [8, 9, 10],
    [20, 30, 27],
    [35, 9, 20]] 
    display the row and column of the number divisible by 5"""

l = [[2, 5, 9],
     [8, 9, 10],
     [20, 30, 27],
     [35, 9, 20]]

for rindex, row in enumerate(l):
    for cindex, col in enumerate(row):
        if col % 5 == 0:
            print((rindex, cindex, col), end=" ")
    print(end="\n")
