#import modules
import os
import csv

#Define variables
tot_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0
candidates = []

#Read CSV
csvpath = os.path.join("Resources/election_data.csv")

#Find the candidates
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        print(f'Our candidates are: {candidates}')

#Count the votes
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        if row[2] == candidates[0]:
            khan +=1
        if row[2] == candidates[1]:
            correy +=1
        if row[2] == candidates[2]:
            li +=1
        if row[2] == candidates[3]:
            otooley +=1

tot_votes = khan + correy + li + otooley


