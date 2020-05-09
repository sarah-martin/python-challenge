import os
import csv

#Create path to collect data from CSV file
budget_csv=os.path.join('Resources', 'budget_data.csv')

#Read in the csv file and skip the header
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    header=next(csvreader)

    #Establish lists to organize information
    months=[]
    monthlyProfit=[]
    monthlyChange=[]

    #Begin looping through csv file
    for row in csvreader:

        #Add months and monthly profit to csvreader
        months.append(row[0])
        monthlyProfit.append(int(row[1]))

        #Determine length of months
        totalMonths=len(months)

        #Determine total net amount of profit
        totalProfit=sum(monthlyProfit)

    for x in range(totalMonths-1):
        monthlyChange.append(monthlyProfit[x]-monthlyProfit[x-1])
        avgChange=round(sum(monthlyChange)/(totalMonths-1),2)
        maxChange=max(monthlyChange)
        minChange=min(monthlyChange)
        
        if minChange==monthlyChange[x]:
            minChange_date=months[x]
        if maxChange==monthlyChange[x]:
            maxChange_date=months[x]

    #Print findings
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfit}")
    print(f"Average Change: {avgChange}")
    print(f"Greatest Increase in Profits: {maxChange_date} (${maxChange}) ")
    print(f"Greatest Decrease: {minChange_date} (${minChange})")

    #write results in text file
    #specify text file path
    output_path=os.path.join('Resources', 'main.txt')

    #Write in the new file
    with open(output_path, "w") as txtfile:

        #Write headers
        txtfile.write("Financial Analysis")
        txtfile.write("-------------------------")
        txtfile.write("")