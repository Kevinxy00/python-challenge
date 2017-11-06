import csv
from datetime import datetime
fullname = []
DOB = []
SSN = []
StateList = []
firstline = True

with open ('employee_data1.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
     #stores all the fullnames in a list, excluding headers
    for rows in reader:
        fullname.append(rows[1])
        DOB.append(rows[2])
        SSN.append(rows[3])
        StateList.append(rows[4])
        
    with open ('employee_data2.csv', mode='r') as csvfile1:
        reader = csv.reader(csvfile1, delimiter = ',')
        next(reader)
        #stores fullnames from 2nd data file into list, excluding headers
        for rows in reader:
            if rows != 1:        
                fullname.append(rows[1])
                DOB.append(rows[2])
                SSN.append(rows[3])
                StateList.append(rows[4])
#       with open ('employee_data_new.csv', mode = 'w') as csvfile1:
#           writer = csv.writer(csvfile1, delimiter = ',')

#splits fullname into two lists [first] and [last]
first, last = zip(*(i.split(' ') for i in fullname))

#format Date of birth from yyyy-mm-dd to mm/dd/yyyy
#!!!compiles but cannot be printed
DOB = (datetime.strptime(i, "%Y-%m-%d").strftime('%m/%d/%Y') for i in DOB)

#format Social security number to be ***-***-####


#format state name to be two letters long


#output new csv with new rows[0] to rows[5] in correct format
print (str(DOB))
