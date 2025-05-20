import requests
from bs4 import BeautifulSoup
import csv

url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
   "Accept-Language": "ko-KR,ko;q=0.9",
   "Referer": "https://www.coupang.com/",
}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
print(res.text)