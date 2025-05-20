import requests
from bs4 import BeautifulSoup
#html파일을 읽어와서 파일html,css 형태로 파싱
with open("w0509/게시판3.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,"lxml")
    
#html 태그 찾는 방법
# data = soup.find("thead")
# ths = data.find_all("th")
# for th in ths:
#     print(th.get_text())

# data = soup.find("div",{"id":"input"})
# data2 = data.nextSibling()
# print(data.div.get_text())

data = soup.find("tbody",{"id":"tbody"})
trs = data.find_all("tr")
print(len(trs))
for tr in trs:
    tds = tr.find_all("td")
    if len(tds)>1:
        for i in range(len(tds)-1):
            print(tds[i].get_text(),end="\t")