import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import random
import pyautogui

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

### 1. 네이버 접속
url = "https://flight.naver.com/flights/domestic/GMP-CJU-20250531/CJU-GMP-20250601?adult=2&fareType=YC"
browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")


while True:

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height: break 
    prev_height = curr_height 

soup = BeautifulSoup(browser.page_source,"lxml")


datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})

for data in datas:

    airline = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()

    times = data.find_all("b",{"class":"route_time__xWu7a"})

    startTime = times[0].get_text().strip()
    starttimeC = times[0].get_text().replace(":","").strip()

    endTime = times[1].get_text().strip()

    price = data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","")
    price = int(price)
    if int(starttimeC)<=1700 or price>=110000:
        continue
    print(f"{airline} {startTime} {endTime} {price}")
print("종료") 
 
input(" ")
