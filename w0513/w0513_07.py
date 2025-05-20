import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time


# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
broswer = webdriver.Chrome(options=options)

soup = BeautifulSoup(broswer.page_source,"lxml")

with open("w0513/fly1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml") 

data = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
maxnum=0
mininum=1000000
contents=[]
for da in data:
    dataA= da.find("b",{"class":"airline_name__0Tw5w"})
    print(dataA.get_text().strip(),end=" ")
    dataT= da.find_all("b",{"class":"route_time__xWu7a"})
    print(dataT[0].get_text().strip(),end=" ")
    print(dataT[1].get_text().strip(),end=" ")
    data1= da.find("i",{"class":"domestic_num__ShOub"})
    if maxnum < int(data1.get_text().replace(",","").strip()):
        maxnum=int(data1.get_text().replace(",","").strip())
    elif mininum > int(data1.get_text().replace(",","").strip()):
        mininum=int(data1.get_text().replace(",","").strip())
    print(data1.get_text().replace(",","").strip())
    contents.append([dataA.get_text().strip(),dataT[0].get_text().strip(),dataT[1].get_text().strip(),int(data1.get_text().replace(",","").strip())])
dd_list = sorted(contents,key = lambda x:x[3]) 
for n in dd_list:
    print(n)

print(f"가장비싼 값:{maxnum} 가장 싼 값:{mininum}")


    
