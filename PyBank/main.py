import os
import csv

#define path where data input file is located
csvpath ='/Users/amyclaman/Downloads/budget_data.csv'

#define variables
row_count = 0
total_profit = 0
greatest_incr_profits = 0
greatest_decr_profits = 0
delta_month_to_month = 0
total_delta = 0
hold_profit = 0

#open the csv file and use it to process the anaylsis
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #read each row, collect, sum and hold necessary data 
    for row in csvreader:
        #count the number of records and add up the profits/losses
        row_count = row_count + 1
        total_profit = total_profit + float(row[1])

        #only start calculating the deltas from row 2 until the end of file
        if row_count > 1:
            delta_month_to_month = float(row[1]) - hold_profit

        #hold the greatest change increase and greatest change decrease as we find them
        if delta_month_to_month > greatest_incr_profits:
            greatest_incr_profits = delta_month_to_month
            hold_greatest_incr_date = row[0]
        elif delta_month_to_month < greatest_decr_profits:
            greatest_decr_profits = delta_month_to_month
            hold_greatest_decr_date = row[0]

        #add up the changes in profits/losses and hold the value for the next row's calculation
        total_delta = total_delta + delta_month_to_month
        hold_profit = float(row[1])

#define string variables to hold output since it's going in two places
output1 = "Financial Analysis"
output2 = "____________________________"
output3 = "Total Months: "+ str(row_count)
output4 = "Total: "+ '${:,.2f}'.format(total_profit)
output5 = "Average Change: "+ '${:,.2f}'.format(total_delta/(row_count - 1))
output6 = "Greatest Increase in Profits: "+ hold_greatest_incr_date + " " + '${:,.2f}'.format(greatest_incr_profits)
output7 = "Greatest Decrease in Profits: "+ hold_greatest_decr_date + " " + '-${:,.2f}'.format(abs(greatest_decr_profits))

print('\n')
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(output6)
print(output7)
print('\n')

# Open the file using "write" mode. Note the output file will be placed in the curren directory.
file = open('PyBankFinancialAnalysis.txt','w') 
 
file.write(output1 + '\n') 
file.write(output2 + '\n') 
file.write(output3 + '\n') 
file.write(output4 + '\n')
file.write(output5 + '\n')
file.write(output6 + '\n')
file.write(output7 + '\n') 
 
file.close() 
