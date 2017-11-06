import csv
fullname = []

fout=open("out.csv","a")
for line in open("employee_data1.csv"):
    fout.write(line).

'''
for num in range(2, 3):
    f = open("employee_data"+str(num)+".csv")
    #f.next() # skip the header
    for line in f:
        if line[1] == "Name":
            f.next()
        else:
            fout.write(line)
    f.close() # not really needed
'''
fout.close()

