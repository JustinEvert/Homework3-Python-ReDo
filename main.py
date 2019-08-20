import os
import csv

#Make file path
PyBank_csv = os.path.join('PyBank_data.csv')

#Define initial variables
Month_Count=0
Profit_Loss_Amount=0
Initial_Revenue=867884
Total_Revenue_Difference=0
Revenue_Change=0
Highest_Monthly_Profit = ["", 0]
Highest_Monthly_Loss = ["", 0]


#Open and read CSV file
#Read the PyBank_Data.csv file
with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvfile)

    for row in csvreader:
        #Calculate Total Months
        Month_Count=Month_Count+1        
	
	#Calculate Total Revenue
        Profit_Loss_Amount += int(row[1])
        
	#Calculate Monthly Revenue Changes
        Revenue_Change = int(row[1]) - Initial_Revenue
        Initial_Revenue = int(row[1])
        Total_Revenue_Difference += Revenue_Change

        #Calculate Max Profit and Month and add to open list ["string", integer]
        if (Revenue_Change > Highest_Monthly_Profit[1]):
            Highest_Monthly_Profit[0] = row[0]
            Highest_Monthly_Profit[1] = Revenue_Change

        #Calculate Max Loss and Month and add to open list ["string", integer]
        if (Revenue_Change < Highest_Monthly_Loss[1]):
            Highest_Monthly_Loss[0] = row[0]
            Highest_Monthly_Loss[1] = Revenue_Change
       
    #Calculate Average changes month to month
    Average_Monthly_Change = round(Total_Revenue_Difference/(Month_Count-1),2)    
        
    print("Financial Analysis")
    print("---------------------------------------")
    print("Total Months: " + str(Month_Count))
    print("Total: " + str(Profit_Loss_Amount))
    print("Average Change: " + str(Average_Monthly_Change))
    print(f"Greatest Increase in Profits: {Highest_Monthly_Profit[0]} (${Highest_Monthly_Profit[1]})")
    print(f"Greatest Decrease in Profits: {Highest_Monthly_Loss[0]} (${Highest_Monthly_Loss[1]})")

    #output - print to txt doc

    textfile= open("main.txt","w")
    textfile.writelines("Total Months " + str(Month_Count) + "\n")
    textfile.writelines("Total: " + str(Profit_Loss_Amount) + "\n")
    textfile.writelines("Average Change: " + str(Average_Monthly_Change) + "\n")
    textfile.writelines(f"Greatest Increase in Profits: {Highest_Monthly_Profit[0]} (${Highest_Monthly_Profit[1]}) \n")
    textfile.writelines(f"Greatest Decrease in Profits: {Highest_Monthly_Loss[0]} (${Highest_Monthly_Loss[1]})")


