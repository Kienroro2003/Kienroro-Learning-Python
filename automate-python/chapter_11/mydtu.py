from selenium import webdriver

url = 'https://mydtu.duytan.edu.vn/'
browser = webdriver.Firefox()
browser.get(url)
username = browser.find_element_by_id('txtUser')
username.send_keys('nguyentrankien')
password = browser.find_element_by_id('txtUser')
username.send_keys('nguyentrankien')