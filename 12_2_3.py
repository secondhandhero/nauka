#prr


import csv

import numpy

ages = []
with open(r'c:\data\pth\prog\temp\lista.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=";")
    for row in readCSV:
        ages.append(int(row[1]))
print(ages)
ages.sort(reverse=1)
print(ages)
m=numpy.median(ages)  # type: real
print(m)
