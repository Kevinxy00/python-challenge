import csv
fullname = []

with open ('employee_data1.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
     #stores all the fullnames in a list
    for rows in reader:
        if rows[1] != "Name":
            fullname.append(rows[1])

    with open ('employee_data2.csv', mode='r') as csvfile1:
        reader = csv.reader(csvfile1, delimiter = ',')
        #stores fullnames from 2nd data file into list
        for rows in reader:
            if rows[1] != "Name":
                fullname.append(rows[1])
            
#       with open ('employee_data_new.csv', mode = 'w') as csvfile1:
#           writer = csv.writer(csvfile1, delimiter = ',')

first, last = zip(*(i.split(' ') for i in fullname))


print (last)
