import requests
from bs4 import BeautifulSoup
import csv

url="https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# ff=open("w0509/stock.csv","w",encoding="utf-8-sig",newline="")
# writer = csv.writer(ff)
# ths = soup.thead.find_all("th")
# fileName=[]
# for th in ths:
#     print(th.get_text(),end="\t")
#     fileName.append(th.get_text())
# writer.writerow(fileName)
trs = soup.tbody.find_all("tr")
print("trs 개수 : ",len(trs))
count = 0
for i,tr in enumerate(trs):
    if count >=5:break
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    print(tds)
    count +=1

    



