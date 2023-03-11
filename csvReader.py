import csv

file = open("../data-file-resource/record.csv" , 'r')

with file:
    read = csv.reader(file)
    for row in read:
     print(row)



file = open("../data-file-resource/record_pipe.csv" , 'r')
with file:
    record_pipe = csv.reader(file)
    for row in record_pipe:
     print(row)