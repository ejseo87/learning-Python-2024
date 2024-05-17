# 코인 정보를 이메일로 보내기
import pybithumb
import smtplib
from email.mime.text import MIMEText
import datetime
import time


def bull_market(ticker):
    ohlcv = pybithumb.get_ohlcv(ticker)
    ma5=ohlcv['close'].rolling(5).mean()
    #print(ohlcv['close'])
    price =  pybithumb.get_current_price(ticker)
    global last_ma5
    last_ma5 = ma5.iloc[-2]
    if price > last_ma5 and price -last_ma5 > stan:
        return 1
    elif price > last_ma5 and price - last_ma5 < stan:
        return 2
    elif price < last_ma5 and price - last_ma5 > stan:
        return 3
    elif price < last_ma5 and price - last_ma5 < stan:
        return 4

    
def send_email(bit, price, dt, last_ma, u_d, num):
    bit = str(bit)
    price = str(price)
    dt = str(dt)
    last_ma = str(last_ma)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    #tls 보안 (필수)
    s.starttls()
    s.login("ejseo87@gmail.com", "kirg lmoj mgyu uwkb")
    if num == 1:
        msg_text = dt + ' 시간의 ' + bit + '의 가격은 ' + price + '이고 평균 가격은 ' + last_ma +\
                    '입니다.\n그리고 ' + u_d + '입니다.\n빨리 매수하세요!'
        msg = MIMEText(msg_text)
        msg['Subject'] = '선택하신 '+ bit + '는 ' + u_d + '입니다.'
        s.sendmail("ejseo87@gmail.com", "ejseo69@naver.com", msg.as_string())
        s.quit()   
    elif num == 3:
        msg_text = dt + ' 시간의 ' + bit + '의 가격은 ' + price + '이고 평균 가격은 ' + last_ma +\
                    '입니다. \n그리고 ' + u_d + '입니다.\n빨리 매도하세요!'
        msg = MIMEText(msg_text)
        msg['Subject'] = '선택하신 '+ bit + '는 ' + u_d + '입니다.'
        s.sendmail("ejseo87@gmail.com", "ejseo69@naver.com", msg.as_string())
        s.quit()   


bit = input("원하는 코인을 입력하세요: ")
stan = int(input("얼마를 기준으로 상승장/하락장을 비교할까요? "))
while True:
    is_bull = bull_market(bit)
    orderbook = pybithumb.get_orderbook(bit)
    ms = int(orderbook["timestamp"])
    dt = datetime.datetime.fromtimestamp(ms / 1000)
    price = pybithumb.get_current_price(bit)

    if is_bull == 1:
        send_email(bit, price, dt, last_ma5, "상승장", is_bull)
    elif is_bull == 3:
        send_email(bit, price, dt, last_ma5, "하락장", is_bull)
    elif is_bull == 2:
        print("현재 가격은 %d 이동평균은 %d로 상승장이지만, %d원 이상이 아닙니다." %(price, last_ma5, stan))
    elif is_bull == 4:
        print("현재 가격은 %d 이동평균은 %d로 하락장이지만, %d원 이하가 아닙니다." %(price, last_ma5, stan))

    time.sleep(600)