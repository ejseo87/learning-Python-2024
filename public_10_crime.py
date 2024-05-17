#공공데이터포털->"범죄" 검색 -> 대검찰청 범죄발생시간 다운로드
import csv
import matplotlib.pyplot as plt

"""
문제1. a= open('crime2017.csv')으로 실행하면 아래의 에러 발생
'utf-8' codec can't decode byte 0xb9 in position 0: invalid start byte
해결은 errors='ignore' 추가로 되었음

문제2. 한글깨짐
https://seong6496.tistory.com/269#google_vignette 참고하여 encoding='cp949'추가함
해결수정사항 : 메모장에서 csv파일 열어서  utf-8로 저장함
"""
a = open('./data/p10_crime2017.csv') #,newline='',encoding='cp949',errors='ignore')

data = csv.reader(a)
header = next(data) # 헤더 불필요하므로 날림

#두번째 코드의 body부분
del(header[0] )
crime_name = [0]*31 
crime_count = [0]*31

count = 0

for row in data:
    row[1:] = map(int, row[1:])
    crime_name[count] = row[0]
    crime_count[count] = row[1:]
    count += 1

plt.rc("font", family = "NanumGothic")
plt.title("시간별 범죄 발생 조사")
for i in range(len(crime_name)):
    plt.plot(header, crime_count[i], label=crime_name[i])
plt.xticks(rotation=90)
plt.legend(fontsize = 7, ncol = 4, loc = "upper left")
plt.show()

"""
#첫번째 코드의 body부분
max = 0
count = 9
i = 0
crime_name = [0] * 31
crime_maxcount = [0]*31 # 범죄분류 31개
crime_time = [0]*31


for row in data:
    row[1:] = map(int, row[1:])
    max = 0
    count = 0
    for num in range(1,10): #열의 갯수
        if max < row[num]:
            max = row[num]
            count = num
        #print(f'max : {max} count : {count} row_num : {row[num]} num : {num}')
    crime_time[i] = header[count] 
    crime_name[i] = row[0]
    crime_maxcount[i] = max
    i += 1

for i in range(len(crime_name)):
    print(f"{crime_time[i]}에 {crime_name[i]}이 최대 {crime_maxcount[i]} 건 발생")
"""
a.close()