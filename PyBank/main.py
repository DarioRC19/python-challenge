#Modules
import os


import csv

#Path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open CSV
with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    #Skips header
    next(csvreader)

    #Setting up variables we are looking for
    total_months = 1

    total_profit = 0

    total_changes = 0
    
    greatest_increase = 0

    greatest_decrease = 9999999999999999999

    #We set these print statements to make it look as close to the example that was given
    print()
    print("Finacial Analysis")
    print()
    print('-' * 20)
    print()
    
    #The CSV reader will start at (2,2) instead of (2,1), helps finding average total change
    row = next(csvreader)

    previous_value = float(row[1])

    #For loop established in CSV file
    for row in csvreader:
        
        #Setting up Counters
        total_months += 1
        total_profit += int(row[1])
        current_value = float(row[1])
       
        change = current_value - previous_value

        previous_value = float(row[1])

        total_changes += change

       #if statement that will give us the month that max increase and decrease happend along with the month it happened in 
        if change > greatest_increase:
            greatest_increase = int(change)
            greatest_increase_month = row[0]
       

        if change < greatest_decrease:
            greatest_decrease = int(change)
            greatest_decrease_month = row[0]
    
    #One is minused from the total months because changes does not occur in the 1st month
    average_profit = (total_changes)  / (total_months - 1)

    #Print function used to print results in cmd
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

#Opened a txt file to the analysis folder that will be writen on
with open('analysis/budget_data.txt','w') as txtfile:

    #Used the txtfile.write function to write the results in the file and \n to organize and make file presentable and legible 
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
    