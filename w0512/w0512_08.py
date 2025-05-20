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
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.melon.com/chart/index.htm"
browser.get(url)
ff = open("w0512/melon.csv","a",encoding="utf-8-sig")
writer = csv.writer(ff)

# 브라우저 실행
driver = webdriver.Chrome(options=options)

soup = BeautifulSoup(browser.page_source,"lxml")

data = soup.find("tbody")
trs = data.find_all("tr")

list=[]
sum = 0
for tr in trs:
    tds = tr.find_all("td")
    list=[]
    for i,td in enumerate(tds):
        if i==1:
            list.append("순위 : "+td.get_text().replace("\n",""))
            continue
        elif i== 5:
            list.append(" 노래 : "+td.find("div",{"class":"ellipsis rank01"}).get_text().replace("\n","")+" 가수: "+td.find("span",{"class":"checkEllipsis"}).get_text().replace(" ",""))
            continue
        elif i==6:
            list.append(" 앨범 : "+td.get_text().replace("\n",""))
            continue
        elif i==7:
            sum += int(td.get_text()[10:].replace("\n","").replace(",",""))
            list.append(" 좋아요 : "+td.get_text()[10:].replace("\n","").replace(",",""))
            continue
        else:
            pass
    print(list)
    writer.writerow(list)
    rank = tds[1].find("span",{"class":"rank"}).get_text()
    imgUrl = tds[3].img["src"]
    img_res=requests.get(imgUrl)
    with open(f"w0512/images/melon_chart{rank}.jpg","w") as f:
        f.write(img_res.content)

    
print(f"좋아요 총합: {sum}")


    # bo = tr.get_text().replace("\n"," ").replace("  "," ").replace("  "," ")
    # print(bo)
# print(tds[6].find("a").get_text().strip())
# print(tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip())
#12