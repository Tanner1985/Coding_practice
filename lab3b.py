#Grab input and set base pay
salesPerson= str(input('Please enter the salespersons name: '))
salesAmount = float(input('Please input the salespersons total sales for the month: '))
vacationDays = float(input('Please input the number of vacation days the salesperson took in the month: '))
monthsAtcompany = float(input('Please input the number of months this salesperson has been with SoftwarePirates: '))
base_pay = 2000
#Set up vacation loss and if bonus is available
if(vacationDays > 3):
    vacationLoss = 200
else:
    vacationLoss = 0
    
if(monthsAtcompany > 3):
    bonusAval = True
else:
    bonusAval = False
#Calculate the commission
if(salesAmount > 10000 and salesAmount < 100001):
    commission = salesAmount * .02
elif(salesAmount > 100000 and salesAmount < 500001):
    commission = salesAmount * .15
elif(salesAmount > 500000 and salesAmount < 1000001):
    commission = salesAmount * .28
elif(salesAmount > 1000000):
    commission = salesAmount * .35
else:
    commission = 0
#Calculate bonuses
if(monthsAtcompany > 59 and salesAmount > 1000000):
    extraBonus = 1000
else:
    extraBonus = 0  
if(salesAmount > 100000 and salesAmount < 500001 and bonusAval == True):
    bonus = 1000
elif(salesAmount > 500000 and salesAmount < 1000001 and bonusAval == True):
    bonus = 5000
elif(salesAmount > 1000000 and bonusAval == True):
    bonus = 100000
else:
    bonus = 0
#Calculate total pay
total_pay = base_pay + commission + bonus + extraBonus - vacationLoss
#Print the results
print(f'Name: {salesPerson}')
print(f'Time with SoftwarePirates : {monthsAtcompany} months')
print(f'Base Salery : ${base_pay:.2f}')
print(f'Commission Earned : ${commission:.2f}')
print(f'Bonus Earned : ${bonus:.2f}')
print(f'Extra Bonus Earned: ${extraBonus:.2f}')
print(f'Deductions : ${vacationLoss:.2f}')
print(f'Total Paycheck : ${total_pay:.2f}')