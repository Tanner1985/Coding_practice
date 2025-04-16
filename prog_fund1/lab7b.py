#Define Constants
STUDENTS = 12
FILENAME = 'names.txt'
#define main
def main():
    #create the list to work with
    studentList = []
    #Loop through input to take student names until the list reaches the correct length
    while STUDENTS > len(studentList):
        name = input('Please enter a students name: ')
        studentList.append(name)
    #Sort the list, then reverse the sort
    studentList.sort()
    studentList.reverse()
    #Append the prof name, then my name to the front of the list
    studentList.append('Polanco')
    studentList.insert(0, 'Tanner')
    #Write and read the file
    writeToFile(FILENAME, studentList)
    readFile(FILENAME)
    #Tuple the list, print the tuple to confirm
    studentTuple = tuple(studentList)
    print(studentTuple)

#Function to write the list to a file
def writeToFile(filename, input):
    with open(filename, 'a') as file:
        for item in input:
            file.write(item + '\n')
#Function to read the file and print its contents
def readFile(filename):
    with open(filename, 'r') as file:
        currentLine = file.readline()
        while currentLine != '':
            print(currentLine, end = '')
            currentLine = file.readline()


#call main
main()