import os
import csv

#Create path to collect data from CSV file
budget_csv=os.path.join('..', 'Resources', 'budget_data.csv' )

#Define the function to use after reading in the csv file
def financialanalysis():

    #Establish lists to organize information
    months=[]
    monthlyProfit=[]
    monthlyChange=[]

    #Begin looping through csv file
    for row in csvreader:

        #Add months and monthly profit to csvreader
        months.append(row[0])
        monthlyProfit.append(row[1])

        #Determine length of months
        totalMonths=int(len(months))

        #Determine total net amount of profit
        totalProfit=int(sum(monthlyProfit))

        



    #Print findings
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: {totalProfit}")
    print(f"Average Change: { }")
    print(f"Greatest Increase in Profits: { } ")
    print(f"Greatest Decrease: { }")

#Read in the csv file and skip the header
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    header=next(csvreader)


