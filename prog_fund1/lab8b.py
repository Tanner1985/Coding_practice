# 1. Input a date in numeric format from the user e.g. mm/dd/yy.

# 2. Examine the month entered by the user. If it is larger than 12 or smaller than 1
# issue an error message and ask for input again. 

# 3. Perform similar validation tests for the date and year. Year must be 2013. (Any
# other year is invalid) In addition, the year must only be two digits long. 

# 4. Once all input has been validated, output the string in long date format. Thus a
# string that was input as 06/01/15 will be output as June 1, 2015.
#Set constants
MONTHNAMES = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

#main function
def main():
    #Get the date and slice out the month, day and year
    date = input('Enter a date (mm/dd/yy): ')
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])
    #Validate month is valid, ask for correction if not
    while month < 1 or month > 12:
        try:
            month = int(input('Invalid month found, please enter correct month in mm format: '))
        except ValueError:
            print('Please only enter a number for the month')
    #Validate day is valid by checking month and then comparing days to the number that month should have, ask for correction if not valid
    if month == 2:
        while day < 1 or day > 28:
            try:
                day = int(input('Invalid day found, please enter correct day in dd format: '))
            except ValueError:
                print('Please only enter a number for the day')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        while day < 1 or day > 30:
            try:
                day = int(input('Invalid day found, please enter correct day in dd format: '))
            except ValueError:
                print('Please only enter a number for the day')
    else:
        while day < 1 or day > 31:
            try:
                day = int(input('Invalid day found, please enter correct day in dd format: '))
            except ValueError:
                print('Please only enter a number for the day')
    #Validate year per instructions only 13            
    while year != 13:
        try:
            year = int(input('Invalid year found, please enter correct year in yy format: '))
        except ValueError:
            print('Please only enter a number for the year')
    #Print the long date format using tuple to pull month name with input month as index
    print(f'{MONTHNAMES[month - 1]} ', day, ', 20', year, sep = '')
    




















#call main
main()