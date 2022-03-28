# 6.6.3 显式等待
from lib2to3.pgen2.driver import Driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get("http://cn.bing.com")

# # driver.find_element_by_id("sb_form_q")

# element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "sb_form_q")))
# element.send_keys("bella")

# sleep(2)
# driver.quit()

locator = (By.NAME, "q")

try:
    # 显式等待
    element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located(locator))
    element[0].send_keys("bella")
except NoSuchElementException as e:
    print(e)
finally:
    sleep(1)
    driver.quit()

    

