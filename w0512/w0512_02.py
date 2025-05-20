import requests
from bs4 import BeautifulSoup
import csv

# url="C:\workspace\webdata\webdata\w0512\screen.html"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# with open("w0512/screen.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
with open("w0512/screen.html","r",encoding="utf-8") as f:
     soup = BeautifulSoup(f,"lxml")
data = soup.find("div",{"id":"morColl"})
print(data)
data2 = data.find("c-flicking")
print(data2)
data3 = data2.find_all("c-doc")
print(len(data3))
