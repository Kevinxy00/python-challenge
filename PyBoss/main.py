#Objective: read in csv files, format &then consolidate all the data,
#write new csv with new data

import csv
from datetime import datetime
import us_state_abbrev
#make sure us_state_abbrev.py is in same folder as this program

empID = []
fullname = []
DOB = []
SSN = []
StateList = []

#stores fullnames et. al. in a list, excluding headers
with open ('employee_data1.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    for rows in reader:
        empID.append(rows[0])
        fullname.append(rows[1])
        DOB.append(rows[2])
        SSN.append(rows[3])
        StateList.append(rows[4])
        
    #stores fullnames et. al. from 2nd data file into list, excluding headers
    with open ('employee_data2.csv', mode='r') as csvfile1:
        reader = csv.reader(csvfile1, delimiter = ',')
        next(reader)
        for rows in reader:
            if rows != 1:        
                empID.append(rows[0])
                fullname.append(rows[1])
                DOB.append(rows[2])
                SSN.append(rows[3])
                StateList.append(rows[4])

#splits fullname into two lists [firstName] and [lastName]
firstName, lastName = zip(*(i.split(' ') for i in fullname))

#format Date of birth from yyyy-mm-dd to mm/dd/yyyy
DOBFixd = []
for i in DOB:
    DOBStore = []
    DOBStore = datetime.strptime(i, "%Y-%m-%d").strftime('%m/%d/%Y')
    DOBFixd.append(DOBStore)
    
#format Social security number to be ***-**-####
SSNFixd = []
HideSSN = []
SSNStars = "***-**-"
for rows in SSN:
    HideSSN = rows.split('-')
    SSNFixd.append(SSNStars + HideSSN[2])
    
#format state name to be two letters long using imported dictionary
StateListFixd = []
for i in StateList:
    SLStore = []
    SLStore = us_state_abbrev.us_state_abbrev[i]
    StateListFixd.append(SLStore)

#zip all rows & output new csv with new rows[0] to rows[5] in correct format
fullData = zip(empID, firstName, lastName, DOBFixd, SSNFixd, StateListFixd)

#writes new csv file, first with new header, then with the consolidated data
with open ('employee_data_new_format.csv', mode = 'w', newline='') as csvfile1:
    writer = csv.writer(csvfile1, delimiter = ',')
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    for row in fullData:
        writer.writerow(row)
   
