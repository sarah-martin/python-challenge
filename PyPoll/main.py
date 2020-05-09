import os
import csv

pypoll_csv=os.path.join('Resources','election_data.csv')

with open(pypoll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=,",")
    header=next(csvreader)

voterID=[]
candidates=[]

for row in csvreader:
    voterID.append(row[0])
    candidates.append(row[2])

    #Count total number of cast votes using len
    votesCast=len(voterID)
