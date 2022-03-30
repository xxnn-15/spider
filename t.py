import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.execute_script('window.open()')

driver.switch_to_window(driver.window_handles[1])
driver.get('https://www.taobao.com')
time.sleep(1)

driver.switch_to_window(driver.window_handles[0])
driver.get('https://python.org')

