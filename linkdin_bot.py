from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
time.sleep(2)
elem = driver.find_element_by_id("session_key-login")
elem.send_keys("ololzfanfan@hotmail.fr")
elem = driver.find_element_by_id("session_password-login")
elem.send_keys("")
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element_by_id("mynetwork-nav-item")
elem.click()
