# import requests, os, bs4
# res = requests.get('http://inventwithpython.com')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# # print(soup.prettify())
#
# elements = soup.select('.btn')
# for element in elements:
#     print(element)

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
linkElem.click()