from config import username, password
from selenium import webdriver
import time


browser = webdriver.Edge()

url = 'http://www.instagram.com'

browser.get(url)

time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(username)

password_field = browser.find_element_by_name('password')
password_field.send_keys(password)

time.sleep(3)
submit_btn = browser.find_element_by_css_selector("button[type='submit']")
submit_btn.click()

# my_button_xpath = "//button"
# browser.find_elements_by_xpath(my_button_xpath)

# CLICK THE BUTTON THAT SAYS NOT NOW
time.sleep(5)
not_now_btn_xpath = "//button [contains(text(), 'Not Now')]"
for btn in browser.find_elements_by_xpath(not_now_btn_xpath):
    btn.click()

follow_button_xpath = "//button[contains(text(), 'Follow')][not (contains(text(), 'Following'))]"
followButtonElements = browser.find_elements_by_xpath(follow_button_xpath)
