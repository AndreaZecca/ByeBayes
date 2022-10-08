import csv
tot=0
with open('./nat_dis.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        if row[2]=='2017':
            tot=tot+int(row[3])

print(tot)