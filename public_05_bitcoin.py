import pybithumb
import time

#최종 코딩

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    price =  pybithumb.get_current_price(ticker)
    last_ma5 = ma5.iloc[-2]
    if price > last_ma5:
        return True
    else:
        return False
    
tickers = pybithumb.get_tickers()

for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker,"상승장")
    else:
        print(ticker, "하락장")


"""
#지금까지 배운 코딩 목록
tickers = pybithumb.get_tickers()

for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, " : ", price)
    time.sleep(0.1)

detail = pybithumb.get_market_detail("BTC")
print(detail)
order=pybithumb.get_orderbook("BTC")
print(order["payment_currency"])
print(order["order_currency"])
bids = order['bids']
asks=order['asks']

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가 : ", price, "매수잔량 : ", quant)

ohlcv = pybithumb.get_ohlcv("BTC")
close=ohlcv['close']
ma5=close.rolling(5).mean()
print(ma5)
"""