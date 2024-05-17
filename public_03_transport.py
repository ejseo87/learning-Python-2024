import csv
import matplotlib.pyplot as plt

a = open("./data/p03_transport.csv")
data = csv.reader(a)

# next()는 1행 제거
next(a)
next(a)

namelist = []
sumlist = []

name = input("호선 선택 : ")
name = name + "호선"
for row in data:
    if name == row[1]:
        row[4:] = map(int, row[4:])
        sum=0
        for i in range(7,10):
            sum+=row[(i-4)*2+5]
        namelist.append(row[3])
        sumlist.append(sum)

plt.rc('font',family="NanumGothic")
plt.bar(namelist, sumlist, color="lightblue")
plt.xticks(rotation=90)
plt.show()


"""1

max = 0

#row에는 3번째 행부터
for row in data:
    row[4:]=map(int,row[4:])
    sum = 0
    for i in range(7,10):
        sum += row[(i-4)*2+5]
    if sum > max:
        max = sum
        trans = row[1]+" "+row[3]
        
print(trans)
"""
a.close()