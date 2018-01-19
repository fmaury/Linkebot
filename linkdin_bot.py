from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

i = 0
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
elem = driver.find_element_by_id("session_key-login")
elem.send_keys("ololzfanfan@hotmail.fr")
elem = driver.find_element_by_id("session_password-login")
elem.send_keys("")
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem = driver.find_element_by_id("mynetwork-nav-item")
elem.click()
time.sleep(3)
while 1 :
    if i == 0 :
        but = driver.find_elements_by_class_name("mn-pymk-list__action-container")
    but[i].click()
    if i != 0 and i % 6 == 0 :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        i = -1
    i += 1
