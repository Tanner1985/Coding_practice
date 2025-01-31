# Get each value for conversion
miles_converter = float(input('William, please input the miles you wish to convert to kilometers'))
fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius'))
gallons_converter = float(input('William, please input the gallons you wish to convert to liters'))
pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms'))
inches_converter = float(input('William, please input the inches you wish to convert to centimeters'))

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