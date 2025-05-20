import requests
from bs4 import BeautifulSoup
# url=""
# headers=""
# res=requests(url,headers=headers)
# soup = BeautifulSoup(res.text,"lmxl")
with open("w0509/a.html","r",encoding="utf-8")as f:
    soup = BeautifulSoup(f,"lxml")
    
print(soup.title)
print(soup.title.get_text())
print(soup.h2)
print(soup.find_all("h2"))
print(soup.find("p",{"id":"p1"}).get_text())
print(soup.find("ul"))
print(soup.find("div",{"class":"c2"}).find("ul").find("li"))
print(soup.find("ul").find_all("li")[1].get_text())
print(soup.find_all("ul")[1].get_text())
    