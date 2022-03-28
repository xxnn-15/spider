## 6.4

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://cn.bing.com/")

sleep(1)

element = driver.find_element_by_id("sb_form_q")
# 在搜索框输入 Selenium
element.send_keys("Selenium")
sleep(2)

# 输入 Ctrl+A
element.send_keys(Keys.CONTROL, 'a')
sleep(2)

# 输入删除键
element.send_keys(Keys.BACK_SPACE)
sleep(2)

# 在搜索框输入 bella
element.send_keys("bella")
sleep(2)

# 输入 Ctrl+A
element.send_keys(Keys.CONTROL, 'a')
sleep(2)

# 输入 Ctrl+X
element.send_keys(Keys.CONTROL, 'x')
sleep(2)

# 输入 Ctrl+V
element.send_keys(Keys.CONTROL, 'v')
sleep(2)

# 输入回车键
element.send_keys(Keys.ENTER)
sleep(2)
driver.close()