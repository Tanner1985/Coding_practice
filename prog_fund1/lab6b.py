# Write a program that reads student names and grades from the user and writes them to a file.
def main():
    #Define file name and number of students
    fileName = 'grades.txt'
    numberOfStudents = 12
    #Loop to get student name and grade, writing to file after each set of input
    for i in range(numberOfStudents):
        studentName = getStudentName()
        studentGrade = getStudentGrade()
        writeValue = studentName + ' ' + str(studentGrade)
        writeToFile(writeValue, fileName)
    #Read the file and print the contents            
    readFile(fileName)
#Function to get and return student name
def getStudentName():
    studentName = input('Enter the student name: ')
    return studentName
#Function to get and return grade with exception handling for non numbers and numbers outside of 0-100
def getStudentGrade():
    try:
        studentGrade = float(input('Enter the student grade: '))
    except ValueError:
        print('Invalid input. Please enter a number')
    while studentGrade < 0 or studentGrade > 100:
        print('Grade must be between 0 and 100')
        studentGrade = getStudentGrade() 
    return studentGrade       
#Function to write to file
def writeToFile(writeValue, fileName): 
    myFile = open(fileName, 'a')
    myFile.write(writeValue + '\n')
    myFile.close()  
#Function to read file, print contents, exception handling if file not found, asks for correct file name
def readFile(fileName):
    try:
        myFile = open(fileName, 'r')    
        print(myFile.read())
        myFile.close()
    except FileNotFoundError:
        print('File not found')
        fileName = input('Enter the correct filename: ')
        readFile(fileName)

main()