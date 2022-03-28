from selenium import webdriver
import time
import json

driver = webdriver.Chrome()



# 打开网页
url = "https://www.huya.com/222523"
driver.get(url)

# 最大化
driver.maximize_window()

# 清除打开浏览器后自带的 cookies
driver.delete_all_cookies()

# 加载之前保存的 cookies, driver.add_cookie(cookie_dict) 参数是字典对象
with open('./selenium/cookies/kryst4l_cookies.txt', 'r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)

# 刷新页面
driver.refresh()

# 等一段时间，以确保页面加载完毕
time.sleep(2)

# 播放直播
css_selector = "#player-brower-pause-guide > div.guide > div.btn"
driver.find_element_by_css_selector(css_selector).click()

# 输入弹幕

css_selector = "#pub_msg_input"
driver.find_element_by_css_selector(css_selector).send_keys("测试")

# 发送弹幕
# 等 1s 再发送，以便观察
time.sleep(1)
css_selector = "#msg_send_bt"
driver.find_element_by_css_selector(css_selector).click()

time.sleep(5)
driver.quit()