import time
import pyupbit
import datetime
import pandas
import json
import random
access = "hdrILWr2DzeQqfQwGNRGzd7YlR9szdvI2HAcqxw3"
secret = "SJg4TSKzg68txqNKr2q6A2ByY2QJV09yJZh3eZ16"

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

coinArray = pyupbit.get_tickers(fiat="KRW")
coinArray = random.shuffle(coinArray)
count = 0

def search() :
    global count
   
    try :
        count +=1
        coinArray = pyupbit.get_tickers(fiat="KRW")
        coinArray = list(reversed(coinArray))

        for i in coinArray :
            #1분봉 #200
            df = pyupbit.get_ohlcv(i, "minute1")
            
            #n/2분 전 종가
            ssClose = int(df.iloc[-10]['close'])
            #n분 전 종가
            firstClose = int(df.iloc[-5]['close'])
            #n분 전 거래량
            firstVolume =int(df.iloc[-5]['volume'])
                        #n분 전 거래량
            sVolume =int(df.iloc[-3]['volume'])
            #n/2분 전 종가
            sClose = int(df.iloc[-3]['close'])

            
            #현재 종가
            curClose = int(df.iloc[-1]['close'])
            #현재 거래량
            curVolume = int(df.iloc[-1]['volume'])
            Price = pyupbit.get_current_price(i)
            #print()
            #print("***  "+ i + "   ***")
            #print('처음 종가/거래량' + str(firstClose) + '/' + str(firstVolume))
            #print('현재 종가/거래량' + str(curClose) + '/' + str(curVolume))

            if (firstClose < int(Price) and sClose < int(Price) and ssClose*1.01 < int(Price) and firstVolume * 1.5 < curVolume and sVolume *2 < curVolume) :
                print("!!!!!!!급등코인!!!!!!!!")
                return i
                break
            
    except :
        print("다시조회합니다. {} 회 반복중".format(count))
        time.sleep(2)
        search()


while True: 
    try:
        i = search() #급등코인 결정
        krw = upbit.get_balance("KRW")
        upbit.buy_market_order(i, krw*0.9995)
        print("<<<< " + str(i) + " 구매완료 >>>>")
        
        # 결제 금액 
        firstPrice = pyupbit.get_current_price(i)
        print("구매금액 : " + str(firstPrice))
        
        while True :
            df1 = pyupbit.get_ohlcv(i, "minute1")

            #n분 전 종가
            firstClose = int(df1.iloc[-3]['close'])
            #n분 전 종가
            firstClose2 = int(df1.iloc[-5]['close'])
            #현재 종가
            curClose = int(df1.iloc[-1]['close'])
            
            curPrice = pyupbit.get_current_price(i)
            
            # 최근 5분 전, 3분 전 둘 다 0.5%이상 하락했을때 or 구매가격에서 0.6% 손해봤을때 
            if  (firstClose*0.995 > int(curPrice) and firstClose2*0.995 > int(curPrice))  or firstPrice *0.993 > curPrice:
                useCoin = upbit.get_balance(i)
                upbit.sell_market_order(i, useCoin)
                print("<<<< " + str(i) + " 판매완료 >>>>")
                time.sleep(5)
                print("현재 보유 KRW : " + str(upbit.get_balance("KRW")))
                break
                
            else : time.sleep(5)
        
        print('판매코인 현재가 : ' + str(pyupbit.get_current_price(i)))
        time.sleep(10)
        
    except Exception as e:
        print(e)
        time.sleep(1)