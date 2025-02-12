#Grab input for needed data and set base pay
salesPerson= input('Please enter the salespersons name: ')
salesAmount = float(input('Please input the salespersons total sales for the month: '))
vacationDays = int(input('Please input the number of vacation days the salesperson took in the month: '))
monthsAtcompany = int(input('Please input the number of months this salesperson has been with SoftwarePirates: '))
base_pay = 2000
#Check if salesperson needs a vacation deduction
if vacationDays > 3:
    vacationLoss = 200
else:
    vacationLoss = 0
#Check if salesperson is eligible for a bonus    
if monthsAtcompany > 3:
    bonusAval = True
else:
    bonusAval = False
#Calculate the commission
if salesAmount > 10000 and salesAmount <= 100000:
    commission = salesAmount * 0.02
elif salesAmount > 100000 and salesAmount <= 500000:
    commission = salesAmount * 0.15
elif salesAmount > 500000 and salesAmount <= 1000000:
    commission = salesAmount * 0.28
elif salesAmount > 1000000:
    commission = salesAmount * 0.35
else:
    commission = 0
#Calculate bonuses
if monthsAtcompany > 59 and salesAmount > 1000000:
    extraBonus = 1000
else:
    extraBonus = 0  
if salesAmount > 100000 and salesAmount <= 500000 and bonusAval:
    bonus = 1000
elif salesAmount > 500000 and salesAmount <= 1000000 and bonusAval:
    bonus = 5000
elif salesAmount > 1000000 and bonusAval:
    bonus = 100000
else:
    bonus = 0
#Calculate total pay
total_pay = base_pay + commission + bonus + extraBonus - vacationLoss
#Print the results
print('SoftwarePirates Paycheck')
print(f'Name: {salesPerson}')
print(f'Time with SoftwarePirates : {monthsAtcompany} months')
print(f'Base Salary : ${base_pay:,.2f}')
print(f'Commission Earned : ${commission:,.2f}')
print(f'Bonus Earned : ${bonus:,.2f}')
print(f'Extra Bonus Earned: ${extraBonus:,.2f}')
print(f'Deductions : ${vacationLoss:,.2f}')
print(f'Total Paycheck : ${total_pay:,.2f}')
