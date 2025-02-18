#Set rows and loop, printing a * for the row number minus the outer loops current iteration
rows = 10
for r in range(rows):
    for s in range(rows - r):
        print('*', end='')
    print('')

#Tried with a controled inner while loop 
for r in range (rows):
    stars = 0
    while stars < (rows - r):
        print('*', end = '')
        stars = stars + 1
    print('')

#Double while loop version
lines = 0
stars2 = 0
while lines < rows:
    while stars2 < (rows - lines):
        print('*', end = '')
        stars2 = stars2 + 1
    print('')
    lines = lines + 1
    stars2 = 0