# Modules
import os
import csv
# read the bank file
pybank_in = os.path.join("/Users/anirbanmukherjee/Documents/UNC Homeworks/HW_10052019", "budget_data.csv")

count_month = 0
profit = 0
month_counter = 0
total_change  = 0
change = 0
prior_great_inc = 0
prior_great_dec = 0

with open(pybank_in, newline='') as pybbank:
    pybbank_reader = csv.reader(pybbank, delimiter =',')
    pybbank = next(pybbank_reader)

    for row in pybbank_reader:
        count_month = count_month + 1
        #print(row[1])
        rowdata = int(eval(row[1]))
        profit = profit + rowdata
         
        #calculate total change
        if (month_counter >= 1 ):
            change =  rowdata - prior_profit
            total_change = total_change + change
            
            #determine greatest increase
            if change > prior_great_inc: 
                great_inc_month = row[0]
                great_inc = change
                prior_great_inc = change

            #determine greatest decrease
            if change < prior_great_dec:        
                great_dec_month = row[0]
                great_dec = change      
                prior_great_dec = change

        prior_profit = rowdata # assign profit to the prior profit
        month_counter = month_counter + 1

months = count_month

average_change = round(total_change/(months-1),2)

#formatting year
great_inc_month = great_inc_month.replace('-','-20') 
great_dec_month = great_dec_month.replace('-','-20') 

print("Financial Analysis")
print("------------------------------------------------")
print("Total Months:  " + str(months))
print("Total:  " + "$"+str(profit))
print("Average  Change:  " + "$"+str(average_change))
print("Greatest Increase in Profits: " + great_inc_month + "  $("+str(great_inc)+")")
print("Greatest Decrease in Profits: " + great_dec_month + "  $("+str(great_dec)+")")

#write report
pybank_out = os.path.join("/Users/anirbanmukherjee/Documents/UNC Homeworks/HW_10052019/python-challenge-master/PyBank", "budget_data_out.txt")
with open(pybank_out, 'w', newline='') as csvfilewrite:
    writer = csv.writer(csvfilewrite)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------------------------"])
    writer.writerow(["Total Months:  " + str(months)])
    writer.writerow(["Total:  " + "$"+str(profit)])
    writer.writerow(["Average  Change:  " + "$"+str(average_change)])
    writer.writerow(["Greatest Increase in Profits: " + great_inc_month + "  $("+str(great_inc)+")"])
    writer.writerow(["Greatest Decrease in Profits: " + great_dec_month + "  $("+str(great_dec)+")"])



