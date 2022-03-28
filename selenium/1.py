### 消除报错信息
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# import requests

# r = requests.get('https://www.baidu.com/favicon.ico')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)



from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("bella")
driver.find_element_by_css_selector("#kw").send_keys("bella")
sleep(1)
driver.find_element_by_id("su").click()

driver.quit()  # 关闭浏览器








# from selenium import webdriver
# from time import sleep

# driver= webdriver.Chrome()
# driver.get("http://cn.bing.com/")

# sleep(3)
# print("访问学术页")
# second_url = "https://cn.bing.com/academic?FORM=Z9LHS3"

# print(f"send page is {second_url}")
# driver.get(second_url)
# sleep(1)
# print("返回到Bing首页")
# driver.back()

# sleep(1)
# print("再前进到学术页")
# driver.forward()
# print(driver.title)
# if driver.title == "搜索 学术":
#     print(True)
# else:
#     print(False)

# sleep(3)
# driver.quit()

