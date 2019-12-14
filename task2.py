# with assci code 65-90, 97-122, 48-57 print chracters base on above range with for loop

for i in range(0, 26):
    if i < 11:
        j = i
    print(chr(65+i) + "\t" + chr(97+i) + "\t" + chr(48 + j))
