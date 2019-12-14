""" take input from user if user enter 3

then your output:

1 X 1 =     2 x 1 =     3 x 1 =
1 X 2 =     2 x 2 =     3 x 2 =
1 X 3 =     2 x 3 =     3 x 3 =
1 X 4 =     2 x 4 =     3 x 4 =
1 X 5 =     2 x 5 =     3 x 5 =
1 X 6 =     2 x 6 =     3 x 6 =
1 X 7 =     2 x 7 =     3 x 7 =
1 X 8 =     2 x 8 =     3 x 8 =
1 X 9 =     2 x 9 =     3 x 9 =
1 X 10 =    2 x 10 =    3 x 10 = """

num = eval(input("enter a number"))

for i in range(1, 11):
    for j in range(1, num+1):
        print(j, "X", i, "=", i*j, end="\t")
    print(end="\n")
