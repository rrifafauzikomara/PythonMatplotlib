import matplotlib.pyplot as rifa
import csv

x = []
y = []

with open('rifa.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

rifa.plot(x,y, label='Loaded from file!')
rifa.xlabel('Result')
rifa.ylabel('Amount')
rifa.title('Safety Comparison Diagram')
rifa.legend()
rifa.show()