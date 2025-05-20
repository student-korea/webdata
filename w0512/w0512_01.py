import requests
from bs4 import BeautifulSoup
import csv

url="https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
ff = open("w0512/stock.csv","a",encoding="utf-8-sig")
writer = csv.writer(ff)
# th1 = soup.find("th")
# print(th1)
# print("-"*50)
# ths = soup.find_all("th")
# print(ths)
# print("-"*50)
# tr1 = soup.find("th",{"class":"tr"})
# print(tr1.get_text())
# print("-"*50)

data = soup.find("tbody")
trs = data.find_all("tr")

title = []
tdata = soup.find('thead')
ths = tdata.find_all("th")

for th in ths:
    title.append(th.get_text().strip())
writer.writerow(title)
# tds =trs[1].find_all("td")

# for td in tds:
#     print(td.get_text().strip(),end=" ")
# print()   
# tds2 =trs[2].find_all("td")
# for td in tds2:
#     print(td.get_text().strip(),end=" ")

# for tr in trs:
#     tds = tr.find_all("td")
#     if len(tds) <= 1:
#         continue
#     for i,td in enumerate(tds):
#         if i==3: 
#             em1=td.find("em").get_text().strip()
#             span1=td.find("span",{"class":"tah"}).get_text().strip()
#             print(em1+" "+span1,end=" ")
#             continue        
#         print(td.get_text().strip(),end=" ")
#     print()
#     print("-"*50)
sum =0
for tr in trs:
    tds = tr.find_all("td")
    contents=[]
    if len(tds) <= 1:
        continue
    for i,td in enumerate(tds):
        if i==2: 
            number = td.get_text().strip()
            contents.append(number)
            price = td.get_text().strip().replace(",","")
            sum += int(price)
            print(price)
            continue        
        if i==3: 
            em1=td.find("em").get_text().strip()
            span1=td.find("span",{"class":"tah"}).get_text().strip()
            contents.append(em1+span1)
            print(em1+" "+span1,end=" ")
            continue 
        tcontent = td.get_text().strip()
        contents.append(tcontent)       
        print(td.get_text().strip(),end=" ")
    print()
    writer.writerow(contents)
    print("-"*50)
print(sum)
ff.close()
print("프로그램을 종료합니다.   ")