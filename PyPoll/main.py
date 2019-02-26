import os
import csv

#define path to data input file
csvpath ='/Users/amyclaman/Downloads/election_data.csv'

#define variables
row_count = 0
votes_casted_list = []
highest_pop_vote = 0

#function to count the frequency of certain candidates and return a dictionary w/ the data
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq

#open the csv file and use it to process the anaylsis
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #read each row, collect all votes into a list to parse 
    for row in csvreader:
        row_count = row_count + 1
        votes_casted_list.append(row[2])
        
#call funtion to parse list and count frequencies
candidate_dict = CountFrequency(votes_casted_list)

#print output to screen
print("")
print("Election Results")
print("_" * 30)
print("Total Votes: "+ str(row_count))
print("_" * 30)
for key, val in candidate_dict.items():
    print(key + ": "+ '{:,.2f}'.format(val/row_count * 100) +"% ("+ str(val) + ")")
    if val > highest_pop_vote:
        hold_winner = key
        highest_pop_vote = val
print("_" * 30)
print("Winner: " + hold_winner)
print("_" * 30)
print("")

# Open the file using "write" mode; note file is being placed in current directory
file = open('PyPollElectionResults.txt','w') 

 # Write summary data to text file
file.write('Election Results' + '\n') 
file.write('______________________________' + '\n') 
file.write('Total Votes: ' + str(row_count) + '\n') 
file.write('______________________________' + '\n')
for key, val in candidate_dict.items():
    file.write(key + ': '+ '{:,.2f}'.format(val/row_count * 100) +'% ('+ str(val) + ')'+ '\n')
file.write('______________________________' + '\n')
file.write('Winner: ' + hold_winner + '\n')
file.write('______________________________' + '\n') 
 
file.close() 
