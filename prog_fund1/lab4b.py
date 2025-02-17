#Set rows and loop, printing a * for the row number minus the outer loops current iteration
rows = 7
for r in range(rows):
    for s in range(rows - r):
        print('*', end='')
    print('')

#Another way using multiplication, simpler
for r in range (rows):
    print('*' * (rows-r))

#Tried with a while loop, works. 
for r in range (rows):
    s=0
    while s < (rows - r):
        print('*', end = '')
        s = s + 1
    print()