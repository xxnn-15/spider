### 6.16

from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://cn.bing.com")
driver.maximize_window()

sleep(1)

js = "document.getElementById('sb_form_q').click();"

driver.execute_script(js)
