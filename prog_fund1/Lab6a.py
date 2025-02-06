#Import conversion function
import labConverter6a
#Define Main function, get input and check for validity with loops to confirm input is valid
def main():
    valueChoice = selectMenu()
    convertNum = 0
    badCounter = 0
    if(valueChoice == 1):
        miles_converter = milesInput() 
        while convertNum < 10 and badCounter < 2:               
            if(miles_converter < 0):
                print('Negative number for miles detected. No running backwards please')
                badCounter = badCounter + 1
                miles_converter = milesInput()
            else:
                convertedValue = labConverter6a.milesToKm(miles_converter)
                writeToText(f'William, {miles_converter:.2f} miles is {convertedValue:.2f} kilometers. Quite a long shot huh?') 
                convertNum = convertNum + 1
                miles_converter = milesInput()
        if(badCounter == 2):        
            print('Ran backwards too many times')
        else:
            print('Conversions complete. They can be found in conversions.txt')      

#Function to write the conversions to a text file
def writeToText(writeValue):
    myFile = open('conversions.txt', 'a')
    myFile.write(writeValue + '\n')
    myFile.close()
#Function to print menu and ask for select choice, validates the input is a number between 1 and 5
def selectMenu():
    print('Please select an option from the menu below:')
    print('1. Convert miles to kilometers')
    print('2. Convert fahrenheit to celsius')
    print('3. Convert gallons to liters')
    print('4. Convert pounds to kilograms')
    print('5. Convert inches to centimeters')
    try:
        menuChoice = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid choice. Please enter a number from 1 to 5')
        menuChoice = selectMenu()
    if(menuChoice < 1 or menuChoice > 5):
        print('Invalid choice. Please enter a number from 1 to 5')
        menuChoice = selectMenu()
    else:
        return menuChoice
#Function to get the miles input
def milesInput():
    try:
        miles_converter = float(input('William, please input the miles you wish to convert to kilometers '))
    except ValueError:
        print('Invalid input. Please enter a number')
        miles_converter = milesInput()    
    return miles_converter
        
main()