import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

a=open("./data/p06_ac.csv")
data=csv.reader(a)

num=0
max=0 #사고가 가장 많은 도로를 찾기 위해서
week=[0]*7 #월화수목금토일
#print(week)
for i in range(5): #머리행부터 합계까지 제거 총 5행 제거
    next(a)

for row in data:
    row[3:] = map(int,row[3:])
    #print(row) 
    if num % 3 == 0:
        for i in range(7):
            week[i] += row[i+3]
        #print(week)

    num += 1

plt.rc("font",family="NanumGothic")
plt.plot(["일","월","화","수","목","금","토"],week,'r--')
plt.show()
"""+
for i in  range(len(week)):
    print(week[i])
"""
a.close()
