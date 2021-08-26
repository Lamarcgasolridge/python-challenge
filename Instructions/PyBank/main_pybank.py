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
csv = os.path.join("..", "Resources", "budget_data.csv")

with open(csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv)
    #append rows
    for row in csvreader:
        months.append(row[0])
        tot.append(row[1])
        monthly_change.append(int(row[1]))


    
    
    

