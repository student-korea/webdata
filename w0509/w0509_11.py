import requests
from bs4 import BeautifulSoup
import csv

with open('w0509/join02_info_input.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
ff=open("w0509/list.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)
dts = soup.section.find_all("dt")
fileName=[]
for fd in dts:
    fileName.append(fd.find("label").get_text())
    print(fd.find("label").get_text(),end=" ")
writer.writerow(fileName)


