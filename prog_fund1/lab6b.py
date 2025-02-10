
def main():
    fileName = 'grades.txt'
    writeToText('Something new', fileName)
    writeToText("I'm here to help you with your grades!", fileName)
    readText(fileName)
#Get name and average grade for a student

#Grade can not be below 0 or above 100 - exception handling to ask for input again if invalid  
#Repeat input for 12 students
#Write all output to a file named grades.txt
#Close the output file
#Open the grades.txt, exception handling if file not found, asks for correct file name
#Read the file and print the contents

def getStudentName():
    studentName = input('Enter the student name: ')
    return studentName

def getStudentGrade():
    try:
        studentGrade = float(input('Enter the student grade: '))
    except ValueError:
        print('Invalid input. Please enter a number')
    if studentGrade < 0 or studentGrade > 100:
        print('Grade must be between 0 and 100')
        studentGrade = getStudentGrade()
    else:
        studentGrade = str(studentGrade) 
        return studentGrade       

def writeToText(writeValue, fileName): 
    myFile = open(fileName, 'a')
    myFile.write(writeValue + '\n')
    myFile.close()  

def readText(fileName):
    try:
        myFile = open(fileName, 'r')
        thisLine = myFile.readline()
        while thisLine != '':
            print(thisLine)
            thisLine = myFile.readline()
        myFile.close()
    except FileNotFoundError:
        print('File not found')
        fileName = input('Enter the correct filename: ')
        readText(fileName)

main()