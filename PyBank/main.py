import os


import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    
    next(csvreader)

    total_months = 1

    total_profit = 0

    total_changes = 0
    
    greatest_increase = 0

    greatest_decrease = 9999999999999999999

    print()
    print("Finacial Analysis")
    print()
    print('-' * 20)
    print()
    row = next(csvreader)

    previous_value = float(row[1])

    for row in csvreader:

        total_months += 1
        total_profit += int(row[1])
        current_value = float(row[1])
       
        change = current_value - previous_value

        previous_value = float(row[1])

        total_changes += change

       
        if change > greatest_increase:
            greatest_increase = int(change)
            greatest_increase_month = row[0]
       

        if change < greatest_decrease:
            greatest_decrease = int(change)
            greatest_decrease_month = row[0]

    average_profit = (total_changes)  / (total_months - 1)


    print(f'Total Months: {total_months}')
    print()
    print(f'Total: ${total_profit}')
    print()
    print(f'Average Change: ${average_profit: .2f}')
    print()
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print()
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    print()

with open('analysis/budget_data.txt','w') as txtfile:

    txtfile.write('\n')
    txtfile.write("Finacial Analysis\n")
    txtfile.write('\n')
    txtfile.write(('-' * 20) + '\n')
    txtfile.write('\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write('\n')
    txtfile.write(f'Total: ${total_profit}\n')
    txtfile.write('\n')
    txtfile.write(f'Average Change: ${average_profit: .2f}\n')
    txtfile.write('\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    txtfile.write('\n')
    txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
    txtfile.write('\n')
    