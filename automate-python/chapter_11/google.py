from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class Google:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f59514049%2funable-to-sign-into-google-with-selenium-automation-because-of-this-browser-or')
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://youtube.com')
        sleep(5)


mylike = Google('kienroro281@gmail.com', 'password')
