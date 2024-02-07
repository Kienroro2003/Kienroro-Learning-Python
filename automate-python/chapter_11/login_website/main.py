import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=self.service, options=chrome_options)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_page(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_email(self, username: str, password: str):
        self.add_input(By.TAG_NAME, 'input', username)
        classname = '.'.join(
            'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b'.split(
                ' '))
        self.click_button(By.CLASS_NAME, classname)




browser = Browser('drivers/chromedriver')
browser.open_page('https://gmail.com')
time.sleep(3)
browser.login_email('kienroro281@gmail.com', '')
time.sleep(5)
# browser.close_page()
