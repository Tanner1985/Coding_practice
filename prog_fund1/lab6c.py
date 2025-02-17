#Write data to a file named coffeeInventory.txt with the following descriptions: Blonde Roast, Medium Roast, Flavored Roast, Dark Roast, Costa Rica Tarrazu
#Write the following pounds to go with each of the above descriptions, 15, 21, 10, 12, 18
#Read the file and display the data along with a sum of the total pounds of coffee
#Append the following data to the file: Guatemala Antigua, 22 ; House Blend, 25 ; Decaf House Blend, 16
#Ask if owner wants to modify the file by removing data, if yes, ask for a description to remove and remove it and it's pounds if it exists, otherwise display "That item was not found in the file"
#Ask if the owner wants to delete data from the file, if yes ask for a description to delete, if it exists delete the name and quantity and replace it by asking for a new name and quantiity. If it does not exist, display "That item was not found in the file"
import os
def main():
    #Define file name
    fileName = 'coffeeInventory.txt'
    #Write inital data to file
    startupData = 'Blonde Roast\n15\nMedium Roast\n21\nFlavored Roast\n10\nDark Roast\n12\nCosta Rica Tarrazu\n18'
    writeToFile(startupData, fileName)
    #Read the file and print the contents
    readFile(fileName)
    #Calculate and print the total pounds of coffee
    poundsTotal = totalPounds(fileName)
    print(f'Total pounds of coffee: {poundsTotal}')
    #Append data to file
    appendData = 'Guatemala Antigua\n22\nHouse Blend\n25\nDecaf House Blend\n16'
    writeToFile(appendData, fileName)
    #Ask owner for description to remove
    dataRemove = input('Would you like to remove data from the file? (yes or no): ')
    if dataRemove == 'yes':
        removeData(fileName)
    readFile(fileName)
    #Ask owner for description to delete and replace
    dataModify = input('Would you like to delete and replace data from the file? (yes or no): ')
    if dataModify == 'yes':
        modifyData(fileName)
    readFile(fileName)

#Function to write to file
def writeToFile(writeValue, fileName): 
    myFile = open(fileName, 'a')
    myFile.write(writeValue + '\n')
    myFile.close()
#Function to read file, print contents, exception handling if file not found asks for correct file name
def readFile(fileName):
    try:
        myFile = open(fileName, 'r')    
        print(myFile.read())
        myFile.close()
    except FileNotFoundError:
        print('File not found')
        fileName = input('Enter the correct filename: ')
        readFile(fileName)
#Function to get pounds of coffee from file and print them
def totalPounds(fileName):
    myFile = open(fileName, 'r')
    totalPounds = 0
    for line in myFile:
        try:
            totalPounds = totalPounds + int(line)
        except ValueError:
            totalPounds = totalPounds + 0        
    myFile.close()
    return totalPounds
#Function to remove data from file
def removeData(fileName):
    with open (fileName, 'r') as myFile, open ('temp.txt', 'w') as tempFil:
        found = False
        removeDesc = input('Enter the description to remove: ')
        currentLine = myFile.readline()
        while currentLine != '':
            if removeDesc == currentLine:
                found = True
                currentLine = myFile.readline()
                currentLine = myFile.readline()
            else:
                tempFil.write(currentLine)
                currentLine = myFile.readline()
        if found == True:
            print('Item removed')
        else:
            print('That item was not found in the file')
    os.remove(fileName)
    os.rename('temp.txt', fileName)
#Function to delete and replace data from file
def modifyData(fileName):
    with open (fileName, 'r') as myFile, open ('temp.txt', 'w') as tempFil:
        found = False
        deleteDesc = input('Enter the description to delete: ')
        currentLine = myFile.readline()
        while currentLine != '':
            if deleteDesc == currentLine:
                found = True
                currentLine = myFile.readline()
                currentLine = myFile.readline()
            else:
                tempFil.write(currentLine)
                currentLine = myFile.readline()
        if found == True:
            print('Item deleted')
            newName = input('Enter the new name: ')
            newQuantity = input('Enter the new quantity: ')
            tempFil.write(newName + '\n' + newQuantity + '\n')
        else:
            print('That item was not found in the file')
    os.remove(fileName)
    os.rename('temp.txt', fileName)

main()