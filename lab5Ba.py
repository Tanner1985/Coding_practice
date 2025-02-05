#Import conversion function
import labconverter
#Define Main function, get input and check for validity, then give to function to calculate and return converstion
def main():
   bad_counter = 0
   miles_converter = float(input('William, please input the miles you wish to convert to kilometers '))
   while(miles_converter < 0 and bad_counter < 2):
        print('Negative number for miles detected. No running backwards please')
        miles_converter = float(input('William, please input the miles you wish to convert to kilometers '))
        bad_counter = bad_counter + 1
   if (bad_counter == 2):
        print('Ran backwards too many times')
   else:
        fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius '))
        bad_counter = 0
        while(fahren_converter > 1000 and bad_counter < 2):
            print('To large a number for temperature conversion. No fires please')
            fahren_converter = float(input('William, please input the degrees in fahrenheit you wish to convert to Celsius '))
            bad_counter = bad_counter + 1 
        if(bad_counter == 2):
            print('Too many fires. You may be on the sun')
        else:
            gallons_converter = float(input('William, please input the gallons you wish to convert to liters '))
            bad_counter = 0
            while(gallons_converter < 0 and bad_counter < 2):
                print ('Negative number for gallons detected. Keep hydrated please')
                gallons_converter = float(input('William, please input the gallons you wish to convert to liters '))
                bad_counter = bad_counter + 1 
            if(bad_counter == 2):
                print('Program dehydrated from too many negatives')    
            else: 
                pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms '))
                bad_counter = 0
                while(pounds_converter < 0 and bad_counter < 2):
                    print ('Negative number for pounds detected. Please patient your antigravity technology')
                    pounds_converter = float(input('William, please input the pounds you wish to convert to kilograms '))
                    bad_counter = bad_counter + 1
                if(bad_counter == 2):   
                    print('Too much antigravity, now on the moon')    
                else: 
                    inches_converter = float(input('William, please input the inches you wish to convert to centimeters '))
                    bad_counter = 0
                    while(inches_converter < 0 and bad_counter < 2):
                        print ('Negative number for inches detected. No playing with shrink-rays')
                        inches_converter = float(input('William, please input the inches you wish to convert to centimeters '))
                        bad_counter = bad_counter + 1
                    if(bad_counter == 2):    
                        print('Too much shrinking, can no longer see')    
                    else:
                        print (f'William, {miles_converter} miles is {labconverter.milesToKm(miles_converter):.2f} kilometers. Quite a long shot huh?')
                        print (f'William, {fahren_converter} degrees fahrenheit is {labconverter.FahToCel(fahren_converter):.2f} degrees celsius. That is so cool!')
                        print (f'William, {gallons_converter} gallons comes out to {labconverter.GalToLit(gallons_converter):.2f} liters. Should I turn down the volume?')
                        print (f'William, {pounds_converter} pounds turns into {labconverter.PoundsToKg(pounds_converter):.2f} kilograms. That was some heavy math!')
                        print (f'William, {inches_converter} inches is {labconverter.InchesToCm(inches_converter):.2f} centimeters. I have no more puns, but that was fun!')

main()