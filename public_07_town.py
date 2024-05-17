import csv
import numpy as np

a = open("./data/p07_town.csv")

data = csv.reader(a)

name = input("원하는 지역 : ")

for i  in data:
    if name in i[1]:
        num = np.array(i[4:],dtype=int)
        break

print(num)

a.close()