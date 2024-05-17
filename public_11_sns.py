# <서울 열린데이터광장>에서  sns로 검색 -> 서울시 SNS이용률 통계 -> csv로 다운로드 -> 메모장에서 utf-8로 저장

import csv
import matplotlib.pyplot as plt

markers = ['.', 'o','v','^','<','>','1','2','3','4','s','p','*','x','D']
a = open("./data/p11_sns.csv")

data = csv.reader(a)

header = next(data) #첫번째 줄 header 에 저장
next(data) # 두번째 줄 날림

del header[:2]

#두번째 코드 body
sns_name = []
sns_use = []
for row in data:
    row[2:]=map(float, row[2:])
    sns_name.append(row[1])
    sns_use.append(row[2:])

plt.rc("font", family="NanumGothic")
plt.figure(figsize=(15,8))
for i in range(len(sns_name)):
    plt.plot(header, sns_use[i], label=sns_name[i], marker=markers[i])
plt.title("서울시 SNS 이용률")
plt.legend(fontsize = 9, loc = "upper right", ncols=2)
plt.show()




"""
#첫번째 코드 body
num = 0
sns_facebook=[]
for row in data:
    row[2:] = map(float, row[2:])
    if num == 5:
        print(row)
        for i in range(2, len(row)):
            sns_facebook.append(row[i])
    num += 1

for i in range(len(sns_facebook)):
    print(header[i], sns_facebook[i])

plt.rc("font", family="NanumGothic")
plt.plot(header, sns_facebook, color="red")
plt.show()
"""

a.close()