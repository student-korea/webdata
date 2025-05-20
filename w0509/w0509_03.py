import requests

url="https://finance.naver.com/sise/nxt_sise_market_sum.naver"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res=requests.get(url)
res.raise_for_status()

print(res.text)
with open("w0509/text.html","w",encoding="utf-8") as f:
    f.write(res.text)
print("프로그램 종료")