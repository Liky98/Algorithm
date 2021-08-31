import time
import pyupbit
import datetime
import pandas
import json
import random
import requests
import pandas as pd
import time
import webbrowser
import pyupbit


access = "hdrILWr2DzeQqfQwGNRGzd7YlR9szdvI2HAcqxw3"
secret = "SJg4TSKzg68txqNKr2q6A2ByY2QJV09yJZh3eZ16"

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("화성가보자잇")

#coinArray = pyupbit.get_tickers(fiat="KRW")

maxRSI = 0
minRSI = 100

def searchRSI(settingRSI):
    try :
        tickers = pyupbit.get_tickers(fiat="KRW")
        for symbol in tickers : 
            url = "https://api.upbit.com/v1/candles/minutes/10"

            querystring = {"market":symbol,"count":"500"}

            response = requests.request("GET", url, params=querystring)

            data = response.json()

            df = pd.DataFrame(data)

            df=df.reindex(index=df.index[::-1]).reset_index()

            df['close']=df["trade_price"]


            def rsi(ohlc: pd.DataFrame, period: int = 14):
                ohlc["close"] = ohlc["close"]
                delta = ohlc["close"].diff()

                up, down = delta.copy(), delta.copy()
                up[up < 0] = 0
                down[down > 0] = 0

                _gain = up.ewm(com=(period - 1), min_periods=period).mean()
                _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

                RS = _gain / _loss
                return pd.Series(100 - (100 / (1 + RS)), name="RSI")

            rsi = rsi(df, 14).iloc[-1]
            #print(symbol)
            #print('Upbit 10 minute RSI:', rsi)
            #print('')
            if rsi < settingRSI :
                print("!!과매도 현상 발견!!")
                return symbol
                break
            time.sleep(1)
    except :
        #print("찾는중...")
        time.sleep(2)
        searchRSI()

def roofRSI(symbol) :
    TF = False
    while TF==False :
        url =  "https://api.upbit.com/v1/candles/minutes/10"

        querystring = {"market":symbol,"count":"500"}

        response = requests.request("GET", url, params=querystring)

        data = response.json()

        df = pd.DataFrame(data)

        df=df.reindex(index=df.index[::-1]).reset_index()

        df['close']=df["trade_price"]

        def rsi(ohlc: pd.DataFrame, period: int = 14):
            ohlc["close"] = ohlc["close"]
            delta = ohlc["close"].diff()

            up, down = delta.copy(), delta.copy()
            up[up < 0] = 0
            down[down > 0] = 0

            _gain = up.ewm(com=(period - 1), min_periods=period).mean()
            _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

            RS = _gain / _loss
            return pd.Series(100 - (100 / (1 + RS)), name="RSI")

        rsi = rsi(df, 14).iloc[-1]
        print(symbol)
        print('Upbit 10 minute RSI:', rsi)
        print('')
        time.sleep(3)
        if rsi > 43 :
            print("이제는 팔때야")
            TF = True
            return True
            break

def sellRSI(symbol, rightRSI, firstPrice) :
    global maxRSI
    time.sleep(5)
    url =  "https://api.upbit.com/v1/candles/minutes/10"

    querystring = {"market":symbol,"count":"500"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.reindex(index=df.index[::-1]).reset_index()

    df['close']=df["trade_price"]

    def rsi(ohlc: pd.DataFrame, period: int = 14):
        ohlc["close"] = ohlc["close"]
        delta = ohlc["close"].diff()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        _gain = up.ewm(com=(period - 1), min_periods=period).mean()
        _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

        RS = _gain / _loss
        return pd.Series(100 - (100 / (1 + RS)), name="RSI")

    rsi = rsi(df, 14).iloc[-1]
    #print(symbol)
    #print('Upbit 10 minute RSI:', rsi)
    #print('')
    time.sleep(1)
    nowPrice = pyupbit.get_current_price(symbol)
    
    if maxRSI < rsi :
        maxRSI = rsi
        
    if (int(rsi)+3 < int(maxRSI) and rsi>=30) or rsi>=70 or (nowPrice < firstPrice*0.98): #이전값보다 RSI값이  3 떨어지면
        print("판매완료")
        TF = True
        return True

def buyRSI(symbol, leftSRI) :
    global minRSI
    time.sleep(5)
    url =  "https://api.upbit.com/v1/candles/minutes/10"

    querystring = {"market":symbol,"count":"500"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.reindex(index=df.index[::-1]).reset_index()

    df['close']=df["trade_price"]

    def rsi(ohlc: pd.DataFrame, period: int = 14):
        ohlc["close"] = ohlc["close"]
        delta = ohlc["close"].diff()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        _gain = up.ewm(com=(period - 1), min_periods=period).mean()
        _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

        RS = _gain / _loss
        return pd.Series(100 - (100 / (1 + RS)), name="RSI")

    rsi = rsi(df, 14).iloc[-1]
    #print(symbol)
    #print('Upbit 10 minute RSI:', rsi)
    #print('')
    time.sleep(0.5)
    
    if minRSI > rsi :
        minRSI = rsi
        
    if (int(rsi) > int(minRSI)+1) or rsi <15 or rsi >28 : #직전값+n 보다 커지면
        print("구매완료")
        TF = True
        return True
    # if rsi > 33 :
    #     return -1

def search_onetime(symbol) :
    time.sleep(3)    
    url =  "https://api.upbit.com/v1/candles/minutes/10"

    querystring = {"market":symbol,"count":"500"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()

    df = pd.DataFrame(data)

    df=df.reindex(index=df.index[::-1]).reset_index()

    df['close']=df["trade_price"]

    def rsi(ohlc: pd.DataFrame, period: int = 14):
        ohlc["close"] = ohlc["close"]
        delta = ohlc["close"].diff()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        _gain = up.ewm(com=(period - 1), min_periods=period).mean()
        _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

        RS = _gain / _loss
        return pd.Series(100 - (100 / (1 + RS)), name="RSI")

    rsi = rsi(df, 14).iloc[-1]
    #print(symbol)
    #print('Upbit 10 minute RSI:', rsi)
    #print('')
    
    return rsi


#메인
while True: 
    try:
        maxRSI = 0
        minRSI = 100
        TF = False
        
        i = searchRSI(26) #과매도현상 코인 찾기 #RSI가 n보다 떨어지면
        krw = upbit.get_balance("KRW")
        #print("구매 타이밍 잡는중...")
        while True :
            firstRSI = search_onetime(i)
            time.sleep(10)
            if buyRSI(i,firstRSI) == True :
                upbit.buy_market_order(i, krw*0.9995)
                time.sleep(1)
                print("<<<< " + str(i) + " 구매완료 >>>>")
                break
            #elif buyRSI(i,firstRSI) == -1 :
             #   TF = True
              #  break
            else :
                time.sleep(1)
                
         
        # 결제 금액 
        firstPrice = pyupbit.get_current_price(i)
        time.sleep(1)
        print("구매금액 : " + str(firstPrice))
        
        while True :
            firstRSI = search_onetime(i)
            #time.sleep(15)
            
            # 판매대기
            if  sellRSI(i, firstRSI, firstPrice)== True:
                useCoin = upbit.get_balance(i)
                upbit.sell_market_order(i, useCoin)
                print("<<<< " + str(i) + " 판매완료 >>>>")
                time.sleep(5)
                print("현재 보유 KRW : " + str(upbit.get_balance("KRW")))
                break
                
            else : time.sleep(1)
        
        print('판매코인 현재가 : ' + str(pyupbit.get_current_price(i)))
        print()
        
        time.sleep(5)
        
    except :
        time.sleep(1)
        