#Write data to a file named coffeeInventory.txt with the following descriptions: Blonde Roast, Medium Roast, Flavored Roast, Dark Roast, Costa Rica Tarrazu
#Write the following pounds to go with each of the above descriptions, 15, 21, 10, 12, 18
#Read the file and display the data along with a sum of the total pounds of coffee
#Append the following data to the file: Guatemala Antigua, 22 ; House Blend, 25 ; Decaf House Blend, 16
#Ask if owner wants to modify the file by removing data, if yes, ask for a description to remove and remove it and it's pounds if it exists, otherwise display "That item was not found in the file"
#Ask if the owner wants to delete data from the file, if yes ask for a description to delete, if it exists delete the name and quantity and replace it by asking for a new name and quantiity. If it does not exist, display "That item was not found in the file"

def main():
    #Define file name
    fileName = 'coffeeInventory.txt'
    #Write inital data to file
    startupData = 'Blonde Roast, 15\nMedium Roast, 21\nFlavored Roast, 10\nDark Roast, 12\nCosta Rica Tarrazu, 18'
    writeToFile(startupData, fileName)
    #Read the file and print the contents
    readFile(fileName)
    #Append data to file
    appendData = 'Guatemala Antigua, 22\nHouse Blend, 25\nDecaf House Blend, 16'
    writeToFile(appendData, fileName)




















def writeToFile(writeValue, fileName): 
    myFile = open(fileName, 'a')
    myFile.write(writeValue + '\n')
    myFile.close()
def readFile(fileName):
    try:
        myFile = open(fileName, 'r')    
        print(myFile.read())
        myFile.close()
    except FileNotFoundError:
        print('File not found')
        fileName = input('Enter the correct filename: ')
        readFile(fileName)