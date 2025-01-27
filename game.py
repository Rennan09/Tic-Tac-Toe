board = []

for i in range (3):
    board.append(i + 1)
    print (i + 1, sep=" ", end = "|" )
    if i == 2:
        print ("")
for i in range (3):
    board.append(i + 4)
    print (i + 4, sep=" ", end = "|"  )
    if i == 2:
        print ("")
for i in range (3):
    board.append(i + 7)
    print (i + 7, sep=" ", end = "|" )
#print (board)
