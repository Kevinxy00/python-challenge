import csv
import datetime
import collections

storeBudget = {}


with open ('budget_data_2.csv', mode='r') as csvfile2:
    reader = csv.reader(csvfile2)
    #stores 2nd budget csv file into dictionary
    storeBudget = {rows[0]:rows[1] for rows in reader}
        
with open ('budget_data_1.csv', mode='r') as csvfile1:
    reader = csv.reader(csvfile1)
    #stores 1st budget csv file into dictionary 
    for rows in reader:
        storeBudget[rows[0]] = rows[1]
        
#need to fix dates. Data may be bad as dates in budget_data_2 may lack year.
#fixDates = datetime.datetime.strptime(str(storeBudget.keys()), "%d/%m/%y")

#ordered = collections.OrderedDict(sorted(storeBudget.items(), key=lambda t: t[0]))
print(storeBudget.keys())        


        
