## 测试代理是否可用
import requests
import random
url = 'https://www.baidu.com/'
proxies_list = [
    'https://144.255.49.40:9999',
    'https://60.13.42.15:9999',
    'https://163.204.246.105:9999'
]
ip_list = []
use_ip =random.choice(proxies_list)
proxies = {'http':use_ip}
print("当前使用ip",use_ip)
try:
    wb_data = requests.get(url=url, proxies=proxies)
    flag = True
except:
    proxies_list.remove(proxies['http'])
    flag = False
if flag:
    ip_list.append(proxies['http'])
print("可用ip列表",ip_list)