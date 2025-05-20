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
# url = "https://www.naver.com/"
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)
def newsSearch(nXpath):
    contents=[]
    time.sleep(1)
    # 뉴스부분 클릭
    browser.find_element(By.XPATH,nXpath).click()
    # 웹스크래핑시작
    soup = BeautifulSoup(browser.page_source,"lxml")
    dataC = soup.find("div",{"class":"media_end_head_top"})
    company = dataC.find("span",{"class":"media_end_head_top_logo_text light_type _LAZY_LOADING_ERROR_SHOW"}).get_text()
    print(company)
    data = soup.find("div",{"class":"media_end_head_title"})
    # 뉴스제목출력
    title = data.find("span").get_text()
    print(title)
    contents.append(company+" "+title)
    writer.writerow(contents)
    time.sleep(1)
    # 뒤로 가기
    browser.back()
f = open("w0514/news.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
for i in range(1,13):
    ## 1. 뉴스 클릭
    nXpath = f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i}]/ul/li[1]/div/a'
    newsSearch(nXpath)
    

## 중요부분
recvMail = "onulee@naver.com" #받는사람 주소
password = "7T4XWRX1ESWJ" ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출


### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = "이메일 글자 발송"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "wnslove15@naver.com"
msg['To'] = recvMail
msg['Subject'] = "뉴스정보 보냅니다."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0514/news.csv',"rb") as f:
    #part담기
    part.set_payload(f.read())

#파일첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 
## header 정보
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("wnslove15",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
recvMails = ['wnslove15@naver.com']
s.sendmail("wnslove15@naver.com",recvMails,msg.as_string())
s.quit() 

print("메일발송 완료")
    