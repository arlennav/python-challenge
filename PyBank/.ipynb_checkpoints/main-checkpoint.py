import csv
from pathlib import Path

sourcepath=Path("Resources/03_python_homework_Instructions_PyBank_Resources_budget_data.csv")
destpath=Path("Resources/analysis.txt")

total_number_of_months=0
total_net_amount=0
changelog={}

def print_export_result():
    with open(destpath,'w') as analysisFile:
        result="Financial Analysis\n"
        result+="----------------------------\n"
        #The total number of months included in the dataset
        result+=f"Total Months: {total_number_of_months}\n"
        #The total net amount of "Profit/Losses" over the entire period
        result+=f"Total: ${total_net_amount}\n"
        #The average change in "Profit/Losses" between months over the entire period
        average_change=round(sum(changelog.values())/(total_number_of_months-1),2)
        result+=f"Average  Change: ${average_change}\n"
        #Greatest Increase in Profits
        result+=f"Greatest Increase in Profits: {max(changelog, key=changelog.get)} (${max(changelog.values())})\n"
        #Greatest Decrease in Losses
        result+=f"Greatest Decrease in Losses: {min(changelog, key=changelog.get)} (${min(changelog.values())})\n"
        analysisFile.write(result) 
        print(result)

with open(sourcepath,encoding="utf-8",newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    next(csvreader)

    #first row
    pre_line = next(csvreader)
    while(True):
        try:
            total_number_of_months+=1
            total_net_amount+=int(pre_line[1])
            cur_line = next(csvreader)
            changelog[cur_line[0]]=int(cur_line[1])-int(pre_line[1])
            pre_line = cur_line
        except:
            break

        
print_export_result()

