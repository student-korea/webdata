import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time

# 셀레니움 크롬 자동화 프로그램
browser=webdriver.Chrome()
browser.get("https://www.naver.com")

elem = browser.find_element(By.ID,"query")
elem.send_keys("시가 총액")
elem.send_keys(Keys.ENTER)
#elem = browser.find_element(By.XPATH,"")
time.sleep(2)
elem.click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.back()
time.sleep(2)
browser.refresh()
time.sleep(1)
browser.forward()


input("키보드 출력")