import requests
from bs4 import BeautifulSoup
import csv

with open('w0509/notice_list.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")


ff=open("w0509/list.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)
trs =soup.table.find_all("tr")
for i,tr in enumerate(trs):
    fileName=[]
    if i==0: 
        ths=soup.table.find_all("th")
        for th in ths:
            print(th.get_text(),end="\t")
            fileName.append(th.get_text())
        writer.writerow(fileName) #상단타이틀 List 타입으로 저장
        print()
        continue
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(),end="\t")
        fileName.append(td.get_text())
    writer.writerow(fileName)
    print()
    
print("파일저장 완료")


# for i,tr in enumerate(trs):
#     if i%2==1:
#         print(i)
#         for tr in trs:
#             print(tr.get_text(),end="\t")
