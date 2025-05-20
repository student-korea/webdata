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

## csv파일 생성

#### 메일발송 ####
## 중요부분
recvMail = "wnslove15@naver.com" #받는사람 주소
password = "7T4XWRX1ESWJ" ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출

### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분

with open('w0515/password.html',"r",encoding='utf-8') as f:
    text=f.read()
      
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "wnslove15@naver.com"
msg['To'] = recvMail
msg['Subject'] = "html 보냅니다."



## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("wnslove15",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
recvMails = 'onulee@naver.com'
s.sendmail("wnslove15@naver.com",recvMail,msg.as_string())
s.quit() 

print("메일발송 완료")


input("프로그램 종료(엔터키 입력)")
