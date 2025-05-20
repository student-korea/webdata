import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

url ="https://edu1032.shiningcorp.com/index.php?device=pc&designkits=1"
browser.get(url)
time.sleep(2)

soup =BeautifulSoup(browser.page_source,"lxml")

with open("w0513/temple1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    
input("프로그램 종료 엔터키>>")