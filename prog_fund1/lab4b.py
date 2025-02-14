#Set rows and loop, printing a * for the row number minus the outer loops current iteration
rows = 7
for r in range(rows):
    for s in range(rows - r):
        print('*', end='')
    print('')