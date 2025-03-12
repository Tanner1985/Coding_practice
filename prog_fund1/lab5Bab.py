#Import conversion function
import labConverter
#Define Main function
def main():
    #Start with getting and checking first input, then print converted numbers with imported labConverter as long as inputs are valid
    valid, miles = getInput('miles')
    if valid:
        print (f'William, {miles} miles is {labConverter.milesToKm(miles):.2f} kilometers. Quite a long shot huh?')
        valid, fahren = getInput('fahren')
    if valid:
        print (f'William, {fahren} degrees fahrenheit is {labConverter.FahToCel(fahren):.2f} degrees celsius. That is so cool!')
        valid, gallons = getInput('gallons')
    if valid:
        print (f'William, {gallons} gallons comes out to {labConverter.GalToLit(gallons):.2f} liters. Should I turn down the volume?')
        valid, pounds = getInput('pounds')
    if valid:
        print (f'William, {pounds} pounds turns into {labConverter.PoundsToKg(pounds):.2f} kilograms. That was some heavy math!')
        valid, inches = getInput('inches')
    if valid:
        print (f'William, {inches} inches is {labConverter.InchesToCm(inches):.2f} centimeters. I have no more puns, but that was fun!')      
#Function for getting and checking input based on type of input requested in arguement, set to allow 3 bad inputs before failing
def getInput(convert):
    badInput = 0
    if convert == 'miles':
        mils = float(input('William, please input the miles you wish to convert to kilometers: '))
        while mils < 0 and badInput < 2:
            mils = float(input('Negative number for miles detected. No running backwards please: '))
            badInput = badInput + 1
        if badInput == 2:
            print('Ran backwards too many times')
            return False, mils
        else:
            return True, mils
    elif convert == 'fahren':
        fahren = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius: '))
        while fahren > 1000 and badInput < 2:
            fahren = float(input('To large a number for temperature conversion. No fires please: '))
            badInput = badInput + 1
        if badInput == 2:
            print('Too many fires. You may be on the sun')
            return False, fahren
        else:
            return True, fahren
    elif convert == 'gallons':
        gallons = float(input('William, please input the gallons you wish to convert to liters: '))
        while gallons < 0 and badInput < 2:
            gallons = float(input('Negative number for gallons detected. Keep hydrated please: '))
            badInput = badInput + 1
        if badInput == 2:
            print('Program dehydrated from too many negatives') 
            return False, gallons
        else:
            return True, gallons 
    elif convert == 'pounds':
        pounds = float(input('William, please input the pounds you wish to convert to kilograms: '))
        while pounds < 0 and badInput < 2:
            pounds = float(input('Negative number for pounds detected. Please patent your antigravity technology: '))
            badInput = badInput + 1
        if badInput == 2:
            print('Too much antigravity, now on the moon')  
            return False, pounds
        else:
            return True, pounds    
    elif convert == 'inches':
        inches = float(input('William, please input the inches you wish to convert to centimeters: '))
        while inches < 0 and badInput < 2:
            inches = float(input('Negative number for inches detected. No playing with shrink-rays: '))
            badInput = badInput + 1
        if badInput == 2:
            print('Too much shrinking, can no longer see') 
            return False, inches
        else:
            return True, inches
    else:
        return False, badInput
        

main()