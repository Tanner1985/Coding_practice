#Set up initial variables
grade = 0
numberGrades = 0
totalGrade = 0
#Use a while loop to continue taking input until told getting a -1 as a grade
while grade != -1:
    grade = float(input('Please enter the current students grade: '))
    numberGrades = numberGrades + 1
    totalGrade = totalGrade + grade
    #Check grade and give feedback on their letter value
    if grade == -1:
        print('Escape value entered')
    elif grade >= 90:
        print('You got an A! Great job')
    elif grade >= 80:
        print('You got a B. Not bad at all!')
    elif grade >= 70:
        print('You got a C. A bit more studying may be a good idea')
    elif grade >= 60:
        print('You got a D. You can do better, study a bit more')
    elif grade == -1:
        print('Done entering grades')
    else:
        print('You got an F! Did you study at all?')
#Check if only 1 loop happened to very a valid grade was entered, then respond accordingly with adverage if real grades were entered
if(numberGrades) == 1:
    print ('No Grades entered')
else:
    print(f'The total number of grades was {numberGrades - 1} and the class adverage was {int((totalGrade + 1)/(numberGrades - 1))}')
    