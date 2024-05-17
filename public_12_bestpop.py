#가온 디지털 차트 검색 

import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_html("https://ko.wikipedia.org/wiki/2021%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")

a = pd.DataFrame(a[0]) #주간차트
song = a['노래']

name = song[0] #기준
nlist = [] #이름
clist = [] #몇번 1위

cnt = 1


for i in range(1, len(song)): 
    if name == song[i]:
        cnt += 1
    elif name != song[i]:
        if name in nlist:
            for j in range(len(nlist)):
                if name == nlist[j]:
                    clist[j] += cnt
            cnt = 1
            name = song[i]
        else:
            nlist.append(name)
            clist.append(cnt)
            cnt = 1
            name = song[i]

    if i == len(song) -1: #마지막노래
        nlist.append(name)
        clist.append(cnt)

max = 0
max_num = 0
for i in range(len(nlist)):
    print(nlist[i], clist[i])
    if max < clist[i]:
        max = clist[i]
        max_num = i
        print(f'max = {nlist[max_num]}  ; {clist[max_num]}')

plt.rc("font", family="NanumGothic")
plt.bar(nlist, clist)
plt.xticks(rotation=75)
#plt.legend()
plt.show()





