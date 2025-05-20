import requests 
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/nxt_sise_market_sum.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
print(soup.title)

data=soup.find("div",{"class":"box_type_l3"})
trs = data.tbody.find_all("tr")

print(trs[9])
# for i in range(7,11):
#     print(trs[i].find_all("td")[1].get_text())
