import requests

url = "https://www.melon.com/"
#url = "https://www.daum.net/"
#url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

print(res.text)
with open("w0509/text.html","w",encoding="utf-8") as f:
    f.write()
print("프로그램 종료")
