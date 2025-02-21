#1. Ask the user for their name and their email address before you display the results
#of the conversions.

#2. When the user enters the email address search the string for the @ symbol. If the
#symbol is not found, ask the user to re-enter their email address till they get it right.

#3. When you display the conversion output to the user, you must include the user’s
#name in the output.
# #Get name and email
userName = input('Please enter your name: ')
email = input('Please enter your email:  ')
#Verify @ is in the email
while '@' not in email:
    email = input('No @ found. Please enter a valid email address: ')
# Get each value for conversion and make sure they are valid using a loop to allow for up to 3 attempts at the input
miles_converter = float(input(f'{userName}, please input the miles you wish to convert to kilometers '))
bad_counter = 0
while miles_converter < 0 and bad_counter < 2:
    print('Negative number for miles detected. No running backwards please')
    miles_converter = float(input(f'{userName}, please input the miles you wish to convert to kilometers '))
    bad_counter = bad_counter + 1
if bad_counter == 2:
    print('Ran backwards too many times')
else:
    fahren_converter = float(input(f'{userName}, please input the degrees in fahrenheit you wish to convert to Celsius '))
    bad_counter = 0
    while fahren_converter > 1000 and bad_counter < 2:
        print('To large a number for temperature conversion. No fires please')
        fahren_converter = float(input(f'{userName}, please input the degrees in fahrenheit you wish to convert to Celsius '))
        bad_counter = bad_counter + 1 
    if bad_counter == 2:
        print('Too many fires. You may be on the sun')
    else: 
        gallons_converter = float(input(f'{userName}, please input the gallons you wish to convert to liters '))
        while gallons_converter < 0 and bad_counter < 2:
            print ('Negative number for gallons detected. Keep hydrated please')
            gallons_converter = float(input(f'{userName}, please input the gallons you wish to convert to liters '))
            bad_counter = bad_counter + 1 
        if bad_counter == 2:
            print('Program dehydrated from too many negatives')    
        else:
            pounds_converter = float(input(f'{userName}, please input the pounds you wish to convert to kilograms '))
            while pounds_converter < 0 and bad_counter < 2:
                print ('Negative number for pounds detected. Please patent your antigravity technology')
                pounds_converter = float(input(f'{userName}, please input the pounds you wish to convert to kilograms '))
                bad_counter = bad_counter + 1
            if bad_counter == 2:   
                print('Too much antigravity, now on the moon')    
            else:    
                inches_converter = float(input(f'{userName}, please input the inches you wish to convert to centimeters '))
                while inches_converter < 0 and bad_counter < 2:
                    print ('Negative number for inches detected. No playing with shrink-rays')
                    inches_converter = float(input(f'{userName}, please input the inches you wish to convert to centimeters '))
                    bad_counter = bad_counter + 1
                if bad_counter == 2:    
                    print('Too much shrinking, can no longer see')    
                else:    
#Do math on each value to convert to metric
                    milesToKm = miles_converter * 1.6
                    fahrenheitToC = (fahren_converter - 32) * 5/9
                    gallonsToL = gallons_converter * 3.9
                    poundsToKl = pounds_converter * .45
                    inchesToCm = inches_converter * 2.54

#Return all the converted values with bad puns
                    print (f'{userName}, {miles_converter} miles is {milesToKm:.2f} kilometers. Quite a long shot huh?')
                    print (f'{userName}, {fahren_converter} degrees fahrenheit is {fahrenheitToC:.2f} degrees celsius. That is so cool!')
                    print (f'{userName}, {gallons_converter} gallons comes out to {gallonsToL:.2f} liters. Should I turn down the volume?')
                    print (f'{userName}, {pounds_converter} pounds turns into {poundsToKl:.2f} kilograms. That was some heavy math!')
                    print (f'{userName}, {inches_converter} inches is {inchesToCm:.2f} centimeters. I have no more puns, but that was fun!')