#import modules
import os
import csv
import statistics

#Create Buckets
tot = []
months = []
monthly_change = []

#Define avg calculation
def average (numbers):
    total = 0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

#Read CSV
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #append rows
    for row in csvreader:
        months.append(row[0])
        tot.append(row[1])
        monthly_change.append(int(row[1]))

    tot_revenue = 0
    for values in tot:
        tot_revenue += int(values)
    print(f'Total Profits/Losses: ${tot_revenue}')
    net_revenue = [j-i for i,j in zip(monthly_change[:-1], monthly_change[1:])]
    print(f'Average Change: ${round(average(net_revenue), 2)}')
    net_revenue.sort(reverse=True)

    print(f'Total Months: {len(months)}')
    print(f'The greatest increase in profits: ${net_revenue[0]}')
    print(f'The greatest decrease in profits: ${net_revenue[len(net_revenue)-1]}')  


#Output Document
    output_path = 'Pybank Analysis.txt'
    
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total Profits/Losses: ${tot_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_revenue),2)}'])
    csvwriter.writerow([f'The greatest increase in profits: ${net_revenue[0]}'])
    csvwriter.writerow([f'The greatest decrease in profits: ${net_revenue[len(net_revenue)-1]}'])


