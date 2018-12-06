import csv
from pathlib import Path

sourcepath=Path("Resources/03_python_homework_Instructions_PyPoll_Resources_election_data.csv")
destpath=Path("Resources/analysis.txt")

total_number_of_votes=0
dicCandidates={}

def print_export_result():
    with open(destpath,'w') as analysisFile:
        result="Election Results\n"
        result+="----------------------------\n"
        result+=f"Total Votes: {total_number_of_votes}\n"
        result+="----------------------------\n"
        for k,v in dicCandidates.items(): 
            candidatewon=round((v/total_number_of_votes),2)*100
            result+=f"{k}: {candidatewon}% ({v})\n"
        result+="----------------------------\n"
        result+=f"Winner: {max(dicCandidates, key=dicCandidates.get)}\n"
        result+="----------------------------\n"
        analysisFile.write(result) 
        print(result)
        
with open(sourcepath,encoding="utf-8",newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    next(csvreader)
    for row in csvreader:
        total_number_of_votes+=1
        if row[2] in dicCandidates.keys():
            dicCandidates[row[2]]+=1
        else:
            dicCandidates[row[2]]=1
    
print_export_result()
