from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
from time import sleep


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://dazi.kukuw.com/"
driver.get(url)

kaishi = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#form > ul:nth-child(8) > li.button > input[type=submit]')))

kaishi.click()

## 获取要打的字
html = driver.page_source
# print(html)
doc = pq(html)
items = doc('#content').children('div').items()
for i, line in enumerate(items):
    words = line.text()
    id = 'i_' + str(i)
    input = driver.find_element(By.ID, id).find_element(By.CLASS_NAME, 'typing')
    input.send_keys(words)
    input.send_keys(Keys.SPACE)
    sleep(1)

