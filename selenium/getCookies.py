## 教程 https://blog.csdn.net/ytraister/article/details/106033630
from selenium import webdriver
import time
import json



urlDict = {}
url_taobao = "https://login.taobao.com/member/login.jhtml?spm=0.1.754894437.1.7483523cE8Xcus&f=top&redirectURL=https%3A%2F%2Fs.taobao.com%2F"
urlDict['taobao'] = url_taobao

url_kryst4l = "https://www.huya.com/222523"
urlDict['kryst4l'] = url_kryst4l

def get_cookies(url, key):
    driver = webdriver.Chrome()
    driver.get(url)
    # 在程序打开网页的 30s 内，手动登录
    for i in range(1,31):
        time.sleep(1)
        print(i)
        
    # 以 json 字符串的形式保存 cookies
    with open(f"./selenium/cookies/{key}_cookies.txt", 'w') as f:
        f.write(json.dumps(driver.get_cookies()))
    
    driver.close()

if __name__ == '__main__':
    for i, key in enumerate(urlDict.keys()):
        print(f"{i:<5}{key:<10}")

    index = int(input("输入想要获取的url的索引\n"))
    key = list(urlDict.keys())[index]
    url = urlDict[key]
    print(url)
    get_cookies(url, key)
