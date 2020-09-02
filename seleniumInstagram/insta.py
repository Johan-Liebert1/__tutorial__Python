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
# time.sleep(5)
# not_now_btn_xpath = "//button [contains(text(), 'Not Now')]"
# for btn in browser.find_elements_by_xpath(not_now_btn_xpath):
#     btn.click()

time.sleep(2)
the_rock_url = 'https://www.instagram.com/therock'
browser.get(the_rock_url)


post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"
post_xpath_str   = "//a[contains(@href, '/p/')]" 
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link = None

if len(post_links) > 0:
    post_link = post_links[0]

if post_link is not None:
    post_href = post_link.get_attribute("href")
    browser.get(post_href)


video_elements = browser.find_elements_by_xpath("//video")
image_elements = browser.find_elements_by_xpath("//img")

follow_button_xpath = "//button[contains(text(), 'Follow')][not (contains(text(), 'Following'))]"
followButtonElements = browser.find_elements_by_xpath(follow_button_xpath)



