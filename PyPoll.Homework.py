import os
import csv


csvpath= os.path.join("Resources", "election_data.csv")
votes_casted = 0
canidates = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for column in csvreader:
        votes_casted += 1
        canidates.append(column[2])
    votes = {}
    for canidate in canidates:
        if canidate in votes:
            votes[canidate] += 1
        else:
            votes[canidate] = 1

contestants_sorted = sorted(
    votes.items(), 
    key=lambda contestant: contestant[1], 
    reverse = True
)
khanpercent = int(votes.get("Khan")) / votes_casted * 100
Correypercent = int(votes.get('Correy')) / votes_casted * 100 
Lipercent = int(votes.get('Li')) / votes_casted * 100
OTooleypercent = int(votes.get("O'Tooley")) / votes_casted * 100

khan = int(votes.get("Khan"))
Correy= int(votes.get('Correy'))
Li = int(votes.get('Li')) 
OTooley = int(votes.get("O'Tooley"))


print("-----------------------------------")
print(f'Total Votes: {votes_casted}')
print("-----------------------------------")
print(f'"Khan:" {round(khanpercent,4)}% {(khan)}')
print(f'"Correy:" {round(Correypercent,4)}% {(Correy)}')
print(f'"Li:" {round(Lipercent,4)}% {(Li)}')
print(f'"O`Tooley:" {round(OTooleypercent,4)}% {(OTooley)}')
print("----------------------")
print(f'{contestants_sorted[0]}')
print("----------------------")

with open("PyPoll.txt", "w") as file:
    file.write("```text ")

    file.write("Election Results \n")

    file.write("--------------------------------\n ")

    file.write(f'Total Votes: {votes_casted} \n')
    file.write("-----------------------------------\n")
    file.write(f'"Khan:" {round(khanpercent,4)}% {(khan)}\n')
    file.write(f'"Correy:" {round(Correypercent,4)}% {(Correy)}\n')
    file.write(f'"Li:" {round(Lipercent,4)}% {(Li)}\n')
    file.write(f'"O`Tooley:" {round(OTooleypercent,4)}% {(OTooley)}\n')
    file.write("----------------------\n")
    file.write(f'{contestants_sorted[0]}\n')
    file.write("----------------------\n")
    file.close()