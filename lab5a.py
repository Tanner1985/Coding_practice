#Define Main function, get input for each value and send to function
#for validity and conversion
def main():
   miles_converter = float(input('William, please input the miles you wish to convert to kilometers'))
   milesToKm(miles_converter)
   fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius'))
   FahToCel(fahren_converter)
   gallons_converter = float(input('William, please input the gallons you wish to convert to liters'))
   GalToLit(gallons_converter) 
   pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms'))
   PoundsToKg(pounds_converter) 
   inches_converter = float(input('William, please input the inches you wish to convert to centimeters'))
   InchesToCm(inches_converter)

#Function to check and convert Miles input
def milesToKm(miles_converter):
    bad_counter = 0
    while(miles_converter < 0 and bad_counter < 2):
        print('Negative number for miles detected. No running backwards please')
        miles_converter = float(input('William, please input the miles you wish to convert to kilometers'))
        bad_counter = bad_counter + 1
    if (bad_counter == 2):
        print('Too many bad inputs. Please try again later')
    else:
        milToKm = miles_converter * 1.6
        print (f'William, {miles_converter} miles is {milToKm:.2f} kilometers. Quite a long shot huh?')
        return
#Function to check and convert Fahrenhit
def FahToCel(fahren_converter):
    bad_counter = 0
    while(fahren_converter > 1000 and bad_counter < 2):
        print('To large a number for temperature conversion. No fires please')
        fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius'))
        bad_counter = bad_counter + 1 
    if(bad_counter == 2):
        print('Too many bad inputs. Please try again later')
    else:
        fahrenheitToC = (fahren_converter - 32) * 5/9
        print (f'William, {fahren_converter} degrees fahrenheit is {fahrenheitToC:.2f} degrees celsius. That is so cool!')
        return
#Function to check and convert Gallons input    
def GalToLit(gallons_converter):
    bad_counter = 0
    while(gallons_converter < 0 and bad_counter < 2):
            print ('Negative number for gallons detected. Keep hydrated please')
            gallons_converter = float(input('William, please input the gallons you wish to convert to liters'))
            bad_counter = bad_counter + 1 
    if(bad_counter == 2):
            print('Too many bad inputs. Please try again later')    
    else:
        gallonsToL = gallons_converter * 3.9
        print (f'William, {gallons_converter} gallons comes out to {gallonsToL:.2f} liters. Should I turn down the volume?')
        return
#Function to check and convert Pounds input
def PoundsToKg(pounds_converter):
    bad_counter = 0
    while(pounds_converter < 0 and bad_counter < 2):
        print ('Negative number for pounds detected. Please patient your antigravity technology')
        pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms'))
        bad_counter = bad_counter + 1
    if(bad_counter == 2):   
                print('Too many bad inputs. Please try again later')    
    else:
        poundsToKl = pounds_converter * .45
        print (f'William, {pounds_converter} pounds turns into {poundsToKl:.2f} kilograms. That was some heavy math!')
        return
#Function to check and convert Inches    
def InchesToCm(inches_converter):
    bad_counter = 0
    while(inches_converter < 0 and bad_counter < 2):
        print ('Negative number for inches detected. No playing with shrink-rays')
        inches_converter = float(input('William, please input the inches you wish to convert to centimeters'))
        bad_counter = bad_counter + 1
    if(bad_counter == 2):    
        print('Too many bad inputs. Please try again later')    
    else:
        inchesToCm = inches_converter * 2.54
        print (f'William, {inches_converter} inches is {inchesToCm:.2f} centimeters. I have no more puns, but that was fun!')
        return

main()