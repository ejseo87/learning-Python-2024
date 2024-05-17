import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import plotly.express as px


pytrends = TrendReq(hl='en-US', tz=360) #미국
keyword_list = ['tesla', 'bitcoin', 'google']
pytrends.build_payload(keyword_list, cat=0, timeframe='today 5-y', geo='KR', gprop='youtube') #유튜브 검색
df = pytrends.interest_over_time() #시간 경과에 따른 관심
df = df.drop(['isPartial'], axis=1) #삭제, 무엇을 "isPartial"
#print(df)

plt.figure(figsize=(20,10))
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['font.size'] = 15

plt.plot(df.index, df['tesla'], label='tesla')
plt.plot(df.index, df['bitcoin'], label='bitcoin')
plt.plot(df.index, df['google'], label='google')

plt.legend(loc='upper left')
plt.title('tesla, bitcoin, google Youtube 검색량', fontsize=18)
plt.show()

""" 
#1번 코딩
pytrends = TrendReq(hl='ko', tz=540) #한국
keyword_list = ['Python', 'c#', 'flutter']
pytrends.build_payload(keyword_list, cat=0, timeframe='today 5-y', geo='KR') 
data = pytrends.interest_over_time() #시간 경과에 따른 관심
data = data.reset_index() #누락데이터 방지
print(data.head(20)) #앞 20개 데이터만 출력
#그래프 그리기
figure = px.line(data, x="date", y=keyword_list, title='구글 트렌드')
figure.show()
"""