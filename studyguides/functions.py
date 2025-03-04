#This is a set of functions made for testing how functions and returns work
#Take not of the variable names as they are passed back and forth. Mess with them and see what happens
def main():
    #Grab some input to check
    truth = input('Enter True or False: ')
    #Using a function directly as part of the if statement
    #function returns True/False and the if block will trigger accordingly
    if isThisTrue(truth):
        thisWasTrue()
    else:
        thisWasFalse()
    #Get two numbers
    number1 = float(input('Please Enter a number: '))
    number2 = float(input('Please Enter another number: '))
    #Print their total by using a function inside the print to add them
    print(addNumbers(number1, number2))
    #Grab the total then store it in a variable and print it, same function with inputs swapped stil returns
    total = addNumbers(number2, number1)
    print(total)
    #Call a function to compare the numbers instead of compareing them in the statement itself
    #As the function returns True/False like isThisTrue it will trigger the if statement if True
    if compareNumber(number1, number2):
        print(f'{number1} is greater than {number2}')

#Function returns a boolen value based on a string, boolen stored in a vairable and the vairable is returned 
def isThisTrue(isTrue):
    if isTrue == 'True':
        answer = True
    else:
        answer = False    
    return answer
#Function to add numbers and return total
def addNumbers(number1, number2):
    total = number1 + number2
    return total
#Function to check if a number is bigger than another
#Returns the same values as isThisTrue, but directly instead of via a variable
def compareNumber(num1, num2):
    if num1 > num2:
        return True
    else:
        return False
#Print functions
def thisWasFalse():
    print('That was false')

def thisWasTrue():
    print('That was true')

main()