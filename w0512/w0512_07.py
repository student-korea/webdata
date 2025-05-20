import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.options import Options
import csv
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.melon.com/chart/index.htm"
browser.get(url)


# 브라우저 실행
driver = webdriver.Chrome(options=options)

soup = BeautifulSoup(browser.page_source,"lxml")
with open("w0512/coupang1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    
with open("w0512/coupang1.html","r",encoding="utf-8") as f:
    f.write(soup.prettify())