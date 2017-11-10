import csv

''' !!! Make sure csv file is spelled right and in the right
location relative to this main.py '''
with open ('raw_data/election_data_2.csv', mode='r', newline = '') as electDat:
    ElecRead = csv.reader(electDat, delimiter = ',')
    next(ElecRead) #to skip the headers
    
    
    VCount = 0 #number of total votes
    CandList = [] #List of names
    CandVotesList = [] #List of votes for each candidate
    CandPercList = [] #List of percentage of votes won for each candidate
    
    for row in ElecRead:
        #tallies up total votes   
        VCount += 1

        #sets Current Candidate as specific column in the read csv
        CurrCand = row[2]
        
        #store unique candidate names and adds blank spot to list of total votes     
        if CurrCand not in CandList:
            CandList.append(CurrCand)
            CandVotesList.append(0)
            
        #tally and store votes for each candidate
        if CurrCand in CandList:
            for i in range(len(CandList)):
                if CurrCand == CandList[i]:
                    CandVotesList[i] += 1
        #skips anomalies, just in case
        else:
            next(ElecRead)

    #Get percentage of votes for each candidate and store in var
    for i in range(len(CandVotesList)):
        PercVote = 0
        PercVote = (CandVotesList[i] / VCount)*100
        CandPercList.append(PercVote)

    #Finds the winner
    winVoteNum = 0
    
    for i in range(len(CandList)):
        if CandVotesList[i] > winVoteNum:
            winVoteNum = CandVotesList[i]
            winName = CandList[i]
        if  (CandVotesList[i] == winVoteNum) and (winName != CandList[i]):
            winName = 'There is a tie!' 
    

#Printing the election results
print('```')
print('Election Results')
print('---------------------')
print('Total Votes: ' + str(VCount))
print('---------------------')
for i in range(len(CandList)):
    print(CandList[i] + ': ' + str(round(CandPercList[i], 2)) + '%' + ' (' + str(CandVotesList[i]) + ')')
print('---------------------')
print('Winner: ' + winName)
print('---------------------')
print('```')

