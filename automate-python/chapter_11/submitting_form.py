from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests, bs4
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://gmail.com')
# res = requests.get('http://gmail.com')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
classname = '.'.join('VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b'.split(' '))
# print(classname)
# print(soup.prettify())
# print(soup.select(classname))
emailElem = browser.find_element(By.TAG_NAME, 'input')
emailElem.send_keys('kienroro281@gmail.com')
button = browser.find_element(By.CLASS_NAME, classname)
button.click()
# emailElem.submit()