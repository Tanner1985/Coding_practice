#Set of file manipulation tests to mess around with

def main():
    yourFile = input('Please give a file name to use: ')
    firstLine = input('Type something you would like to put in a file: ')
    writeLineToFile(yourFile ,firstLine)
    readFile(yourFile)
















#Writes a single line to a file
def writeLineToFile(fileName, line):
    myFile = open (fileName, 'a')
    myFile.write(line +'\n')
    myFile.close
#Function to read and print entire file given
def readFile(filename):
    with open (filename, 'r') as readingFile:
        print(readingFile.read())
def findLine(filename, line):
    with open (filename, 'r') as findLineFile:
        currentLine = findLineFile.readline()
        while line != currentLine or currentLine != '':
            currentLine = findLineFile.readline()
        if currentLine == line:
            print('Line found in file!')
        else:
            print('Line not found in file')


main()