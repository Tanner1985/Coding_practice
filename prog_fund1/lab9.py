# For this portion of the lab, you will create a new program for Professor Polanco (this is the
# last one!) Create a class named Student that holds the following data about a student:

# 1. Name
# 2. Student ID number
# 3. GPA
# 4. Expected grade in this course
# 5. Full time or part time

# Create five student objects from this class and pass data to fill in the class data above.
# Besides creating the objects, you will write a menu-driven program that
# performs the following tasks: 
# 1. Look up and print the student GPA
# 2. Add a new student to the class
# 3. Change the GPA of a student
# 4. Change the expected grade of a student
# 5. Print the data of all the students in a tabular format
# 6. Quit the program Save all the files that you create in this program with appropriate
# file names. 
#import and constants
import student
NUMBEROFSTUDENTS = 5


def main():
    #create the students we will be using and store them in a list
    students = []
    choice = 0
    for i in range (NUMBEROFSTUDENTS):
        students.append(createNewStudent())
    while choice != 6:     
        choice = menu()
        if choice == 1:
            lookUpGPA(students)
        elif choice == 2:
            students.append(createNewStudent())
        elif choice == 3:
            changeGPA(students)
        elif choice == 4:
            changeExpect(students)
        elif choice == 5:
            displayData(students)
        else:
            print('Exiting the program')

#Function to create a new student using the Student Class
def createNewStudent():
    name = input('Please enter the students name: ')
    id = input('Please enter the students ID: ')
    gpa = input('Please enter the students GPA: ')
    expectGrade = input('Please enter the students expected grade: ')
    fullOrPart = input('Please enter if the student is full or part time: ')
    return student.Student(name, id, gpa, expectGrade, fullOrPart)
#Main menu function
def menu():
    pick = 0
    print('Please choose from the following options')
    print('Look up a students GPA: 1')
    print('Add a new student: 2')
    print('Change a students GPA: 3')
    print('Change a students expected grade: 4')
    print('Print all student data: 5')
    print('Exit the program: 6')
    print('-----------------------------------------')
    while pick < 1 or pick > 6:
        try:
            pick = int(input('Please enter your choice: '))
        except:
            print('Invalid menu choice, please use 1 - 6')
    return pick
#Function to search a list of student objects for a specific ID, then return the GPA and name for that ID
def lookUpGPA(list):
    lookID = input('Please enter the ID of a student to display their GPA: ')
    found = False
    for student in (list):
        id = student.getID()
        if id == lookID:
            gpa = student.getGPA()
            name = student.getName()
            found = True
    if found:
        print('-----------------------------------------')
        print(f'The GPA for {name} is {gpa}')
        print('-----------------------------------------')
    else:        
        print('No student with that ID found')
#Fucntion to search the list of students by ID then update the GPA of the student
def changeGPA(list):
    lookID = input('Please enter the ID of a student to change their GPA: ')
    found = False
    for student in (list):
        id = student.getID()
        if id == lookID:
            student.setGPA()
            found = True
    if not found:
        print('No student with that ID found')
#Function to search the list of students by ID and update their expected grade        
def changeExpect(list):
    lookID = input('Please enter the ID of a student to change their Expected Grade: ')
    found = False
    for student in (list):
        id = student.getID()
        if id == lookID:
            student.setExpecGrade()
            found = True
    if not found:
        print('No student with that ID found')

#Function to print a table of students stored in the student list
def displayData(list):
    print('Name\t\t', 'Student ID\t\t', 'GPA\t', 'Expected Grade\t', 'Full Time or Part Time')
    print('-------------------------------------------------------------------------------------')
    for student in (list):
        print(f'{student.getName()}\t\t{student.getID()}\t\t{student.getGPA()}\t\t{student.getExpecGrade()}\t\t{student.getFullorPart()}')
        print('-------------------------------------------------------------------------------------')

main()



