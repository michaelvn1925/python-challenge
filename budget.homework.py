import os
import csv


csvpath= os.path.join("Resources", "budget_data.csv")
date_month = 0
profit_loss = 0
first_number = 0
change = 0
changes = 0
Average = 0
changeMax = 0
changeMin = 0
mcount = 0
total = 0
change_list = []
month = []


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for column in csvreader:
        date_month += 1
        profit_loss  += int(column[1])
        month.append(column[0])
        
        if(date_month == 1):
            first_number = column[1]
        else:
            change = int(column[1]) - int(first_number)
            first_number = column[1]
            change_list.append((change))
            Average += change
            changes += 1
            
            max_decrease = min(change_list)
            decrease = change_list.index(max_decrease)
            month_decrease = month[decrease + 1]
            
            max_increase = max(change_list)
            increase = change_list.index(max_increase)
            month_increase = month[increase + 1]
new_average = (Average /changes)
         
print("```text")
print("Financial Analysis")
print("--------------------------------")
print(f'Total Months: {date_month}')
print(f'Total: ${profit_loss}')
print("Average Change:" + " " + str(round(new_average,2)))
print(f'Greatest Increase in profits: {month_increase} (${max(change_list)})')
print(f'Greatest Decrease in profits: {month_decrease} (${min(change_list)})')

file = open("testfile.txt","w")
file.write("```text \n")

file.write("Financial Analysis \n")

file.write("-------------------------------- \n")

file.write(f'Total Months: {date_month} \n')

file.write(f'Total: ${profit_loss} \n')
file.write("Average Change: " + " " + str(round(new_average,2)))
file.write(f'Greatest Increase in profits: {month_increase} (${max(change_list)})\n')
file.write(f'Greatest Decrease in profits: {month_decrease} (${min(change_list)})\n')
file.close()
