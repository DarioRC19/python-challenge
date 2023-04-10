#Modules
import os


import csv

#Path for file
csvpath = os.path.join('Resources', 'election_data.csv')

#Open CSV
with open(csvpath) as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips header
    next(csvreader)

    #Blank dictionary established where info from file will be used/stored
    election = {}

    #For loop that combined all in info in row2
    for row in csvreader:

        name = row[2]

        #IF statement that made a counter for each name to get a total for each & overall total in the election dictionary
        if name in election:
            election[name] += 1
        else:
            election[name] = 1 

#Total variable establiehed 
total = 0

#We set these print statements to make it look as close to the example that was given
print()
print("Election Results")
print()
print( '-' * 20 )

#Max used to find name with most votes
winner = max(election, key=election.get)

#Used For loop on the election dictionary to get total sum the votes
for name,count in election.items():
    total += count

#print function to print results
print(f'Total Votes: {total}')   
print() 
print( '-' * 20 )

#Used for loop in election dictonary to find how much each canidate got used info to get percentage
for name,count in election.items():
    percent = (count / total) *100

    #Used Print Function to print the variables below into the cmd
    print(f"{name}: {percent: .3f}% ({count})")
    print()

print('-' * 20)
#Print function used to print winner
print(f'Winner: {winner}')


#Opened a txt file to the analysis folder that will be writen on
with open('analysis/election_data.txt','w') as txtfile:
    
    #Used the txtfile.write the results in the file and \n to organize and make file presentable and legible
    txtfile.write('\n')
    txtfile.write('Election Results\n')
    txtfile.write('\n')
    txtfile.write( ('-' * 20) + '\n' )

    winner = max(election, key=election.get)

    for name,count in election.items():
        total += count

    txtfile.write(f'Total Votes: {total}\n')   
    txtfile.write('\n') 
    txtfile.write(  ('-' * 20) + '\n'  )
    for name,count in election.items():
        percent = round((count / total) *100, 3)
        
        txtfile.write(f'{name}: {percent: .3f}% ({count})\n')
        txtfile.write('\n')

    txtfile.write( ('-' * 20) + '\n' )
    txtfile.write(f'Winner: {winner}\n')

    
    

    


    


