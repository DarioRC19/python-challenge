
import os


import csv


csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath) as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    election = {}

    for row in csvreader:

        name = row[2]

        if name in election:
            election[name] += 1
        else:
            election[name] = 1 

total = 0

print()
print("Election Results")
print()
print( '-' * 20 )

winner = max(election, key=election.get)

for name,count in election.items():
    total += count

print(f'Total Votes: {total}')   
print() 
print( '-' * 20 )
for name,count in election.items():
    percent = (count / total) *100
    
    print(f"{name}: {percent: .3f}% ({count})")
    print()

print('-' * 20)
print(f'Winner: {winner}')



with open('analysis/election_data.txt','w') as txtfile:
    
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

    
    

    


    


