from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ramdom
import time
import sys

i = 0
if len(sys.argv) < 4 :
    print('Usage : python Linkebot.py --login "login" --password "password"')
    sys.exit(0)
if (sys.argv[1] == "--login" and sys.argv[3]  == "--password") or  (sys.argv[3] == "--login" and sys.argv[1]  == "--password") :
    try :
        driver = webdriver.Firefox()
        driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
        elem = driver.find_element_by_id("session_key-login")
        elem.send_keys(sys.argv[2])
        elem = driver.find_element_by_id("session_password-login")
        elem.send_keys(sys.argv[4])
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
            time.sleep(random.randrange(1, 3, 0.5))
            i += 1
    except Exception :
        print("Wrong login or password")
else :
    print('Usage : python Linkebot.py --login "login" --password "password"')
