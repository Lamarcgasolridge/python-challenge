#import modules
import os
import csv
import statistics

#Create Buckets
tot = []
months = []
monthly_change = []

def average (numbers):
    total = 0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

#Read CSV
csv = os.path.join("..", "Resources", "budget_data.csv")




    
    
    

