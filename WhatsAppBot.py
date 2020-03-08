import time

from selenium import webdriver

chrome_browser = webdriver.Chrome(
    executable_path='/Users/akhileshsingh/Desktop/Drivers/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

user_name = 'My'

user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = chrome_browser.find_element_by_xpath('//div[@class="_13mgZ"]')
message_box.send_keys('Hey, I am your whatsapp bot')

message_box = chrome_browser.find_element_by_xpath('//button[@class="_3M-N-"]')
message_box.click()
