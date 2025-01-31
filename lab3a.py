# Get each value for conversion and make sure they are valid
miles_converter = float(input('William, please input the miles you wish to convert to kilometers'))
if(miles_converter < 0):
    print('Negative number for miles detected. No running backwards please')
else:
    fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius'))
    if(fahren_converter > 1000):
        print('To large a number for temperature conversion. No fires please')
    else: 
        gallons_converter = float(input('William, please input the gallons you wish to convert to liters'))
        if(gallons_converter < 0):
            print ('Negative number for gallons detected. Keep hydrated please')
        else:
            pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms'))
            if(pounds_converter < 0):
                print ('Negative number for pounds detected. Please patient your antigravity technology')
            else:    
                inches_converter = float(input('William, please input the inches you wish to convert to centimeters'))
                if(inches_converter < 0):
                    print ('Negative number for inches detected. No playing with shrink-rays')
                else:    
#Do math on each value to convert to metric
                    milesToKm = miles_converter * 1.6
                    fahrenheitToC = (fahren_converter - 32) * 5/9
                    gallonsToL = gallons_converter * 3.9
                    poundsToKl = pounds_converter * .45
                    inchesToCm = inches_converter * 2.54


#Return all the converted values with bad puns
                    print (f'William, {miles_converter} miles is {milesToKm:.2f} kilometers. Quite a long shot huh?')
                    print (f'William, {fahren_converter} degrees fahrenheit is {fahrenheitToC:.2f} degrees celsius. That is so cool!')
                    print (f'William, {gallons_converter} gallons comes out to {gallonsToL:.2f} liters. Should I turn down the volume?')
                    print (f'William, {pounds_converter} pounds turns into {poundsToKl:.2f} kilograms. That was some heavy math!')
                    print (f'William, {inches_converter} inches is {inchesToCm:.2f} centimeters. I have no more puns, but that was fun!')