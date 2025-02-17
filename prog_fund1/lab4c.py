#Set up initial variables
moreGrades = 'yes'
numberGrades = 0
totalGrade = 0
#Use a while loop to continue taking input until told to stop
while moreGrades != 'no':
    grade = float(input('Please enter the current students grade: '))
    numberGrades = numberGrades + 1
    totalGrade = totalGrade + grade
    #Check grade and give feedback on their letter value
    if grade >= 90:
        print('You got an A! Great job')
    elif grade >= 80:
        print('You got a B. Not bad at all!')
    elif grade >= 70:
        print('You got a C. A bit more studying may be a good idea')
    elif grade >= 60:
        print('You got a D. You can do better, study a bit more')
    else:
        print('You got an F! Did you study at all?')
    #Ask if they want to break the input loop
    moreGrades = input('Would you like to enter another grade? yes or no : ')
#print the final number of grades and the adverage 
print(f'The total number of grades was {numberGrades} and the class adverage was {int(totalGrade/numberGrades)}')
    