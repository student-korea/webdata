import requests

#res = requests.get("https://www.google.com/")
#res = requests.get("https://www.melon.com/")
res = requests.get("https://www.naver.com/")
if res.status_code==200:
    print("정상적인 프로그램 진행")
    print(res)
    # 응답코드 : 200 이면 정상, 400: 페이지 없음 접근제한 500: 서버오류
    print("응답코드 : ",res.status_code)
    res.raise_for_status() #에러시 종료
    print(res.text)
else:
    print("프로그램 종료")
