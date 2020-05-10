#Incorporate csv module
import os
import csv

#Create path to collect data from CSV file
budget_csv=os.path.join('Resources', 'budget_data.csv')

#Read in the csv file and store the header
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

    #loop through monthly profit column
    for x in range(totalMonths-1):

        #add the monthly change based off current cell and next cell    
        monthlyChange.append(monthlyProfit[x]-monthlyProfit[x-1])

        #use monthly change to calculate average change, max change, and min change
        avgChange=round(sum(monthlyChange)/(totalMonths-1),2)
        maxChange=max(monthlyChange)
        minChange=min(monthlyChange)
        
        #find and store the date associate with the min and max changes
        if minChange==monthlyChange[x]:
            minChange_date=months[x]
        if maxChange==monthlyChange[x]:
            maxChange_date=months[x]

    #Print findings in terminal
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfit}")
    print(f"Average Change: {avgChange}")
    print(f"Greatest Increase in Profits: {maxChange_date} (${maxChange})")
    print(f"Greatest Decrease in Profits: {minChange_date} (${minChange})")

    #write results in text file
    #specify text file path
    output_path=os.path.join('Resources', 'main.txt')

    #Write in the new file
    with open(output_path, "w") as txtfile:

        #Write findings in txt file
        txtfile.write("Financial Analysis\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Months: {totalMonths}\n")
        txtfile.write(f"Total: ${totalProfit}\n")
        txtfile.write(f"Average Change: {avgChange}\n")
        txtfile.write(f"Greatest Increase in Profits: {maxChange_date} (${maxChange})\n")
        txtfile.write(f"Greatest Decrease in Profits: {minChange_date} (${minChange})\n")