import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
import random
# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
### 네이버 자동 로그인 메일 쓰기
url = "https://www.naver.com/"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기
### 셀레니움은 자동화 프로그램
# 클릭이벤트
# elem = browser.find_element(By.CLASS_NAME,"MyView-module__naver_logo____Y442")
# elem.click()
## 글자입력 이벤트
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()

time.sleep(random.uniform(3,5))
elem = browser.find_element(By.ID,"id")
input_js = 'document.getElementById("id").value = "onulee";\
            document.getElementById("pw").value = "aaa1111";'
time.sleep(random.uniform(3,5))
browser.execute_script(input_js)
time.sleep(random.uniform(3,5))

# elem = browser.find_element(By.ID,"id")
# elem.send_keys("onulee")
# time.sleep(random.uniform(3,5))
# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("1111")
# time.sleep(random.uniform(3,5))
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()
input("프로그램 종료(엔터키)")

