
def main():
    writeToText('Something new')
    writeToText("I'm here to help you with your grades!")
    readText()
#Get name and average grade for a student

#Grade can not be below 0 or above 100 - exception handling to ask for input again if invalid  
#Repeat input for 12 students
#Write all output to a file named grades.txt
#Close the output file
#Open the grades.txt, exception handling if file not found, asks for correct file name
#Read the file and print the contents

def writeToText(writeValue): 
    myFile = open('grades.txt', 'a')
    myFile.write(writeValue + '\n')
    myFile.close()  

def readText():
    try:
        myFile = open('grades.txt')
        thisLine = myFile.readline()
        while thisLine != '':
            print(thisLine)
            thisLine = myFile.readline()
        myFile.close()
    except FileNotFoundError:
        print('File not found')

main()