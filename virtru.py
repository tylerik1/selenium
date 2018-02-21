'''
Created on Feb 15, 2018

@author: erik
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys

def virtru_test():
    '''
    send email from gmail to hotmail using virtru and verify the contents
    '''
    
    #load extension
    options = webdriver.ChromeOptions()
    options.add_extension("C:\Python27\selenium\chrome_with_addon\Virtru-Email-Encryption-_v7.1.10.0.crx")
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(5)
    
    
    
    #log into gmail and compose a mail
    driver.get("https://mail.google.com/mail")
    email = driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("xxxx")
    next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    password = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys("xxxx")
    time.sleep(2)
    next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    skip = driver.find_element_by_xpath('/html/body/div[17]/div[2]/div[2]/div[4]/a').click()
    time.sleep(2)
    compose = driver.find_element_by_xpath('//*[@id=":46"]/div/div').click()
    time.sleep(2)
    slider = driver.find_element_by_xpath('//*[@id=":98"]/div[1]/div[3]/div[2]/div[1]/div').click()
    time.sleep(2)
    activate = driver.find_element_by_xpath('//*[@id=":98"]/table/tbody/tr[1]/div/div/div/div[2]/span/a').click()
    time.sleep(2)
    recipient = driver.find_element_by_xpath('//*[@id=":9e"]').send_keys('xxxx')
    time.sleep(2)
    subject = driver.find_element_by_xpath('//*[@id=":8w"]').send_keys('test')
    time.sleep(2)
    body = driver.find_element_by_xpath('//*[@id=":a0"]').send_keys("this is a test to send an email using virtru")
    time.sleep(2)
    
    #attach the file and send
    attach = driver.find_element_by_xpath('//*[@id=":al"]').click()
    time.sleep(2)
    app = Application().Connect(title=u'Open', class_name='#32770')
    window = app.Open
    combobox = window.ComboBox
    combobox.Click()
    SendKeys("test_attachment.txt")
    button = window[u'&Open']
    button.Click()
    time.sleep(2)
    send = driver.find_element_by_xpath('//*[@id=":6i"]/div[2]').click()
    time.sleep(2)
    open = driver.find_element_by_xpath('//*[@id=":3a"]').click()
    time.sleep(2)
    
    
    #log into hotmail and check the mail
    driver.get("https://hotmail.com")
    sign_in = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[2]/div/div').click()
    email = driver.find_element_by_xpath('//*[@id="i0116"]').send_keys("xxxx")
    next = driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(2)
    password = driver.find_element_by_xpath('//*[@id="i0118"]').send_keys("xxxx")
    sign_in = driver.find_element_by_xpath('//*[@id="idSIButton9"]').click() 
    open = driver.find_element_by_xpath('//*[@id="_ariaId_30"]').click()
    time.sleep(3)
    unlock = driver.find_element_by_xpath('//*[@id="Item.MessageUniqueBody"]/div/div/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a').click()
    time.sleep(2)
    
    #switch to the new tab that was opened
    handle = driver.window_handles[1]
    driver.switch_to_window(handle)
    time.sleep(2)
    
    #in case of a fresh login, validate email
    try:
        my_email = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[3]/a[1]/div/span').click()
        time.sleep(2)
        login = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[3]/a[1]/span').click()
        time.sleep(5)
    except:
        pass
    
    #Verify body
    value = driver.find_element_by_id("tdf-body").text
    if not "this is a test to send an email using virtru" in value:
        return "FAIL"
    
    #Verify attachment
    view_attachment = driver.find_element_by_class_name('virtru-attachment-content').click()
    time.sleep(4)
    value = driver.find_element_by_xpath('//*[@id="fullscreen-container"]/div/div[1]/div[2]/div/div/div/div[3]/div').text
    if not "this is a test attachment" in value:
        return "FAIL"
    
    return "PASS"
 
    
    
print virtru_test()    
    
    
    
