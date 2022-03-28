### 6.16.3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time
import json

driver = webdriver.Chrome()

# 打开网页
url = "https://www.huya.com/222523"
driver.get(url)

# 最大化
driver.maximize_window()

# 清楚打开浏览器后自带的 cookies
driver.delete_all_cookies()

# 加载之前保存的 cookies, driver.add_cookie(cookie_dict) 参数是字典对象
with open('./selenium/cookies.txt', 'r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)

# 刷新页面
driver.refresh()

time.sleep(1)

# 播放
driver.find_element_by_css_selector("#player-brower-pause-guide > div.guide > div.btn > p").click()
time.sleep(3)


# 鼠标移动到视频播放窗口，以触发暂停键
video_widows = driver.find_element_by_css_selector("#player-mouse-event-wrap").text
ActionChains(driver).move_to_element(video_widows).perform()

# 暂停播放 3s
video_play = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'player-btn')))
video_play.click()
time.sleep(3)

# 继续播放 3s
ActionChains(driver).move_to_element(video_widows).perform()
video_play.click()
time.sleep(3)

# 关闭浏览器
driver.quit()






