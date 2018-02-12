from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

def log(driver, login, passwd):
  driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
  elem = driver.find_element_by_id("session_key-login")
  elem.send_keys(login)
  elem = driver.find_element_by_id("session_password-login")
  elem.send_keys(passwd)
  elem.send_keys(Keys.RETURN)
  time.sleep(6)
  elem = driver.find_element_by_id("mynetwork-nav-item")
  elem.click()
  time.sleep(6)

def add(driver):
  i = 0
  while 1 :
      if i == 0 :
          but = driver.find_elements_by_class_name("mn-pymk-list__action-container")
      but[i].click()
      if i != 0 and i % 6 == 0 :
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          time.sleep(4)
          i = -1
      i += 1

if __name__ == "__main__":
    login = str(raw_input("Email: "))
    passwd = str(getpass.getpass())
    driver = webdriver.Firefox()
    log(driver, login, passwd)
    add(driver)
    driver.close()
