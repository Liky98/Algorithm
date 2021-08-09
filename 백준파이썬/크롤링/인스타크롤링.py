from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import pyautogui

baseURL = 'https://www.instagram.com/'
plusURL = input('입력 : ')
url = baseURL + quote_plus(baseURL)

#############################################로그인
driver = webdriver.Chrome('백준파이썬\크롤링\chromedriver_win32\chromedriver.exe')
usr = "tset"
pwd = "test01"
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
elem = driver.find_element_by_name("username")
elem.send_keys(usr)
elem = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(3)

##########################################주소이동
searchURL = 'https://www.instagram.com/explore/tags/'
url = searchURL + quote_plus(plusURL)
driver.get(url)

time.sleep(3)

# 파이오토로 설정눌러주는거 할려했는데 안하고 url주소 바꿈
# a1= pyautogui.locateCenterOnScreen('submit.PNG') 
# pyautogui.moveTo(a1) #화면 캡쳐한 곳 가운데로 이동
# pyautogui.doubleClickclick() #한번 클릭
# time.sleep(1) #1초 대기

html = driver.page_source #페이지 소스 가져옴.
soup = BeautifulSoup(html, "html.parser") #웹페이지 분석.

insta = soup.select('.v1Nh3.kIKUG._bz0w')#클래스명이 v1Nh3인 것을 선택함.
n= 1  #얘는 사진제목정할때 1씩 오르면서 저장할려고 설정함.

for i in insta : #위에 선택한 클래스는 많기 때문에 배열(list) 형태임.
    #print('https://www.instagram.com' + i.a['href']) # a태그의 href 값 
    imgUrl = i.select_one('.KL4Bh').img['src'] #클래스명이 KL4Bh인 곳의 img태그의 src를 가져옴
    with urlopen(imgUrl) as f : #가져온 이미지 링크를 오픈함. 이걸 f라 함.
       # print(imgUrl)
        with open('D:/VSCODE/IIP_VSCODE/IIP_VSCODE/백준파이썬/크롤링/testFolder/' + plusURL + str(n)+ '.jpg', 'wb') as h : #write binary #폴더는 미리 만들어놔야함.
            img = f.read() #img 라는 변수는 위에 가져온 링크를 읽는 거임.
            h.write(img)  #img 변수를 위에처럼 write함.
    n +=1 #제목1, 제목2 , ... 
        # print(imgUrl)
        # print()
driver.close