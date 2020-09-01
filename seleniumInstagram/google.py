from selenium import webdriver
import time

browser = webdriver.Edge()

url = 'https://www.google.com'

browser.get(url)

name = 'q'

search_area = browser.find_element_by_name(name)

time.sleep(2)

search_area.send_keys("search this")

submit_btn = browser.find_element_by_css_selector("input[type='submit']")

time.sleep(2)

submit_btn.click()

username = 'yemiye7989'
password = 'newpass'