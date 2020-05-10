#Incorporate csv module
import os
import csv

#Create file path
pypoll_csv=os.path.join('Resources','election_data.csv')

#Read the csv file and store the header
with open(pypoll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    #Create variables to hold data
    totalVotes=[]
    canidateName=[]
    canidateOptions=[]
    canidateVotes=[]
    canidatePercent=[]

    #For each row,
    for row in csvreader:

        #Store total votes
        totalVotes.append(row[2])

        #Count total number of cast votes using len to count the list length
        votesCast=len(totalVotes)

    for canidateName in totalVotes:

        #Store the canidate name from each row
        canidateName=row[2]

        #If the canidate is not already in the list,
        if canidateName not in canidateOptions:

            #Add them to the list of options and begin counting their votes
            canidateOptions.append(canidateName)
            canidateVotes.append(0)
            canidatePercent.append(0)

        for x in range(len(canidateOptions)):
            if canidateOptions[x]==canidateName:
                canidateVotes[x]+=1

    #Loop through canidate votes to find the winner
    for x in range(len(canidatePercent)):
        canidatePercent[x]=round((canidateVotes[x]/votesCast)*100,3)

        if max(canidateVotes)==canidateVotes[x]:
            winner=canidateOptions[x]

    #Print results to terminal
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {votesCast}")
    print("---------------------")
    for x in range(len(canidateOptions)):
        print(f"{canidateOptions[x]}: {canidatePercent[x]}% ({canidateVotes[x]})")
    print("---------------------")
    
    #write results in text file
    #specify text file path
    output_path=os.path.join('Resources', 'main.txt')

    #Open file for writing
    with open(output_path, "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("---------------------\n")
        txtfile.write(f"Total Votes: {votesCast}\n")
        txtfile.write("---------------------\n")
        for x in range(len(canidateOptions)):
            txtfile.write(f"{canidateOptions[x]}: {canidatePercent[x]}% ({canidateVotes[x]})\n")
        txtfile.write("---------------------\n")