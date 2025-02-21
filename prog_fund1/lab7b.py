# Requirements:
# 1. You must use functions and pass the list in and out of the function.
# 2. The input must be interactive from the keyboard. You will take input for 12 students.
# 3. You will input the students’ name and insert/append each name in a list named students. (LO 1,2)
# 4. Sort the list in alphabetical order. (LO 2)
# 5. Sort the list again in reverse order. (LO 2)
# 6. Append the instructor’s name on to the list. (LO 2)
# 7. Insert your own name at the beginning of the list. (LO 2)
# 8. Write the list to a file. (LO 2)
# 9. Display the contents of the file named names.txt.
# 10.Convert the list to a Tuple. (LO 2, 5)
#Define Constants
STUDENTS = 3
FILENAME = 'names.txt'
#define main
def main():
    studentList = []
    while STUDENTS > len(studentList):
        name = input('Please enter a students name: ')
        studentList.append(name)
    studentList.sort()
    studentList.reverse()
    studentList.append('Polanco')
    studentList.insert(0, 'Tanner')
    writeToFile(FILENAME, studentList)
    readFile(FILENAME)
    studentTuple = tuple(studentList)
    print(studentTuple)


def writeToFile(filename, input):
    with open(filename, 'a') as file:
        for item in input:
            file.write(item + '\n')

def readFile(filename):
    with open(filename, 'r') as file:
        currentLine = file.readline()
        while currentLine != '':
            print(currentLine, end = '')
            currentLine = file.readline()


#call main
main()