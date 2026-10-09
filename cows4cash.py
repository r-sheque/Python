print('Menu:' '\n')
print('============''\n\n' )
print('Whole Milk Cow: $100') 
print('Skim Milk Cow: $90')
print('Half-and-Half Cow: $95')
print('Chocolate Milk Cow: $110' '\n\n')
num1 = 100
num2= 90
num3= 95
num4= 110
cow1 = int(input('How many whole milk cows do you want?:'))
cow2 = int(input('How many skim milk cows do you want?:'))
cow3 = int(input('How many half-and-half cows do you want?:'))
cow4 = int(input('Hw many chocolate milk cows do you want?:'))
print('\n\n')
print('Whole:' + str(cow1) + '\t' + 'Skim:' + str(cow2) + '\t' + 'Half-and-half:' + str(cow3) + '\t' + 'Chocolate:' + str(cow4) + '\t' )
total = (cow1 * num1) + (cow2 * num2) + (cow3 * num3) + (cow4 * num4)
print('Total: $' + str(total))

