#Import conversion function
import labConverter6a
#Define Main function, get input and check for validity with loops to confirm input is valid
def main():
    valueChoice = selectMenu()
    convertNum = 0
    badCounter = 0
    if(valueChoice == 1): 
        while convertNum < 10 and badCounter < 3:
            miles_converter = milesInput()             
            if(miles_converter < 0):
                print('Negative number for miles detected. No running backwards please')
                badCounter = badCounter + 1
            else:
                convertedValue = labConverter6a.milesToKm(miles_converter)
                writeToText(f'William, {miles_converter:.2f} miles is {convertedValue:.2f} kilometers. Quite a long shot huh?') 
                convertNum = convertNum + 1
        if(badCounter == 3):        
            print('Ran backwards too many times')
        else:
            print('Conversions complete. They can be found in conversions.txt')
    elif(valueChoice == 2):
        while convertNum < 10 and badCounter < 3:
            fahren_converter = fahrenheitInput()               
            if(fahren_converter > 1000):
                print('To large a number for temperature conversion. No fires please')
                badCounter = badCounter + 1
            else:
                convertedValue = labConverter6a.FahToCel(fahren_converter)
                writeToText(f'William, {fahren_converter:.2f} degrees fahrenheit is {convertedValue:.2f} degrees celsius. That is so cool?') 
                convertNum = convertNum + 1
        if(badCounter == 3):        
            print('Too many fires. You may be on the sun')
        else:
            print('Conversions complete. They can be found in conversions.txt')  
    elif(valueChoice == 3):
        while convertNum < 10 and badCounter < 3:
            gallons_converter = gallonsInput()               
            if(gallons_converter < 0):
                print('Negative number for gallons detected. Keep hydrated please')
                badCounter = badCounter + 1
            else:
                convertedValue = labConverter6a.GalToLit(gallons_converter)
                writeToText(f'William, {gallons_converter:.2f} gallons comes out to {convertedValue:.2f} liters. Should I turn down the volume?') 
                convertNum = convertNum + 1
        if(badCounter == 3):        
            print('Program dehydrated from too many negatives')
        else:
            print('Conversions complete. They can be found in conversions.txt')
    elif(valueChoice == 4):
        while convertNum < 10 and badCounter < 3:
            pounds_converter = poundsInput()               
            if(pounds_converter < 0):
                print('Negative number for pounds detected. Please patient your antigravity technology')
                badCounter = badCounter + 1
            else:
                convertedValue = labConverter6a.PoundsToKg(pounds_converter)
                writeToText(f'William, {pounds_converter:.2f} pounds turns into {convertedValue:.2f} kilograms. That was some heavy math!') 
                convertNum = convertNum + 1
        if(badCounter == 3):        
            print('Too much antigravity, now on the moon')
        else:
            print('Conversions complete. They can be found in conversions.txt')
    elif(valueChoice == 5):
        while convertNum < 10 and badCounter < 3: 
            inches_converter = inchesInput()              
            if(inches_converter < 0):
                print('Negative number for inches detected. No playing with shrink-rays')
                badCounter = badCounter + 1
            else:
                convertedValue = labConverter6a.InchesToCm(inches_converter)
                writeToText(f'William, {inches_converter:.2f} inches is {convertedValue:.2f} centimeters. I have no more puns, but that was fun!') 
                convertNum = convertNum + 1
        if(badCounter == 3):        
            print('Too much shrinking, can no longer see')
        else:
            print('Conversions complete. They can be found in conversions.txt')  
    else:
        print('Unsure how you got here. Starting over')
        main()  

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
def fahrenheitInput():
    try:
        fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius '))
    except ValueError:
        print('Invalid input. Please enter a number')
        fahren_converter = fahrenheitInput()
    return fahren_converter
def gallonsInput():
    try:
        gallons_converter = float(input('William, please input the gallons you wish to convert to liters '))
    except ValueError:
        print('Invalid input. Please enter a number')
        gallons_converter = gallonsInput()
    return gallons_converter
def poundsInput():
    try:
        pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms '))
    except ValueError:
        print('Invalid input. Please enter a number')
        pounds_converter = poundsInput()
    return pounds_converter
def inchesInput():   
    try:
        inches_converter = float(input('William, please input the inches you wish to convert to centimeters '))
    except ValueError:
        print('Invalid input. Please enter a number')
        inches_converter = inchesInput()
    return inches_converter
        
main()