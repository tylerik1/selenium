'''
Created on Dec 16, 2017

@author: erik
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
driver.get("https://login.live.com")

email = driver.find_element_by_xpath('//*[@id="i0116"]').send_keys("xxxx")

submit = driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()

password = driver.find_element_by_xpath('//*[@id="i0118"]').send_keys("xxxx")

submit = driver.find_element_by_xpath('//*[@id="idSIButton9"]').send_keys(Keys.ENTER)


time.sleep(1)

driver.get("https://bing.com")

query = ["bloomberg", "reddit", "twitter", "facebook", "stack overflow", "weather", "sports", "movies", "games", "funny"]


while len(query) != 0:
    index = random.randint(0,len(query)-1)
    
    clear = driver.find_element_by_xpath('//*[@id="sb_form_q"]').clear()
    
    search = driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys(query.pop(index))
    
    send = driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()
    
    time.sleep(2)
    
    
driver.close()

