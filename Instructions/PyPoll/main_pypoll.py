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

#Vote share calculation
khan_share = khan / tot_votes
correy_share = correy / tot_votes
li_share = li / tot_votes
otooley_share = otooley / tot_votes

#Find winner
winner = max(khan, correy, li, otooley)

if winner == khan:
    winner_id = "Khan"
elif winner == correy:
    winner_id = "Correy"
elif winner == li:
    winner_id = "Li"
elif winner == otooley:
    winner_id = "O'Tooley"

#Output Document
output_path = 'Pypoll Analysis.txt'

with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Votes: {tot_votes}'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Khan: {khan_share:.2%}({khan})'])
    csvwriter.writerow([f'Correy: {correy_share:.2%}({correy})'])
    csvwriter.writerow([f'Li: {li_share:.2%}({li})'])
    csvwriter.writerow([f"O'Tooley: {otooley_share:.2%}({otooley})"])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f"Winner: {winner_id}"])
    csvwriter.writerow(["------------------------------------------------------"])