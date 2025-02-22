#Set constants and import converter
import labConverter
FAHRENSTART = -10
STANDARDSTART = 0
TABLEEND = 101
INCREMENT = 10
#define main
def main():
    #Create a table for Fahrenheit to Celsius
    table = tableCreate(FAHRENSTART, TABLEEND, INCREMENT)
    #Convert the table to Celsius
    convTable = tableConvert('fahtocel', table)
    #print the table
    print('---------------------------------------------------------')
    print('These are the converted values of Fahrenheit to Celsius')
    print('---------------------------------------------------------')
    printTable(table, convTable)
    #Create table for Miles to Kilometers, convert and print
    table = tableCreate(STANDARDSTART, TABLEEND, INCREMENT)
    convTable = tableConvert('miltokilo', table)
    print('---------------------------------------------------------')
    print('These are the converted values of Miles to Kilometers')
    print('---------------------------------------------------------')
    printTable(table, convTable)
    #Create table for Gallons to Liters, convert and print
    table = tableCreate(STANDARDSTART, TABLEEND, INCREMENT)
    convTable = tableConvert('galtolit', table)
    print('---------------------------------------------------------')
    print('These are the converted values of Gallons to Liters')
    print('---------------------------------------------------------')
    printTable(table, convTable)
    #Create table for Pounds to Kilos, convert and print
    table = tableCreate(STANDARDSTART, TABLEEND, INCREMENT)
    convTable = tableConvert('poutokil', table)
    print('---------------------------------------------------------')
    print('These are the converted values of Pounds to Kilograms')
    print('---------------------------------------------------------')
    printTable(table, convTable)
    #Create table for Inches to centimeters, convert and print
    table = tableCreate(STANDARDSTART, TABLEEND, INCREMENT)
    convTable = tableConvert('inctocen', table)
    print('---------------------------------------------------------')
    print('These are the converted values of Inches to Centimeters')
    print('---------------------------------------------------------')
    printTable(table, convTable)

#Function to create first row list for basic values
def tableCreate(start, end, increment):
    table = []
    for index in range(start, end, increment):
        table.append(index)
    return table
#Function to convert the values in the basic table to metric based on the conversion requested
def tableConvert(type, table):
    convTable = []
    if type == 'fahtocel':
        for index in range(len(table)):
            convTable.append (f'{labConverter.FahToCel(table[index]):.2f}')
    elif type == 'miltokilo':
        for index in range(len(table)):
            convTable.append (f'{labConverter.milesToKm(table[index]):.2f}')
    elif type == 'galtolit':
        for index in range(len(table)):
            convTable.append (f'{labConverter.GalToLit(table[index]):.2f}')
    elif type == 'poutokil':
        for index in range(len(table)):
            convTable.append (f'{labConverter.PoundsToKg(table[index]):.2f}')
    elif type == 'inctocen':
        for index in range(len(table)):
            convTable.append (f'{labConverter.InchesToCm(table[index]):.2f}')
    else:
        print('Error, this should not happen')
    return convTable
#Function to combine and print the values of the two tables using tab for formatting
def printTable(table, convTable):
    rows = 2
    cols = len(table)
    combinedTable = [table,
                     convTable]
    for r in range (rows):
        for c in range (cols):
            value = combinedTable [r] [c]
            print(value, end = '\t')
        print()


#call main
main()