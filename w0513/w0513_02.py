import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

url ="https://www.gmarket.co.kr/n/best"
browser.get(url)
time.sleep(2)

soup =BeautifulSoup(browser.page_source,"lxml")

data = soup.find("div",{"id":"container"})
ul = data.find("ul",{"class":"list__best"})
lis =ul.find_all("li")
### 1-10위 제목,가격 출력
### 총합계 가격을 출력하시오.
sum = 0
for li in lis[:10]:
    print(li.find("span",{"class":"box__label-rank"}).get_text()) # 순위
    print(li.find("p",{"class":"box__item-title"}).get_text()) # 제목
    price = li.find("span",{"class":"text__value"}).get_text()
    print(price) # 가격
    price = int(price.replace(",",""))
    sum += price
print(f"총합계 :{sum:,d}")

input("프로그램 종료 엔터키>>")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# url = "https://www.gmarket.co.kr/n/best"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")