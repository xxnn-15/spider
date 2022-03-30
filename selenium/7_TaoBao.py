"""
    python selenium 练习，爬取淘宝搜索 ipad 商品的前 20页内容，并将结果保存到 mysql 中
"""
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
from pyquery import PyQuery as pq
import pymysql
import pymongo

# 无界面模式
chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(driver, 10)

# 必须要先指定 url 打开浏览器，再加载 cookies
# 必须首先加载网站，这样Selenium 才能知道cookie 属于哪个网站，即使加载网站的行为对我们没任何用处
url = "https://s.taobao.com/search?initiative_id=staobaoz_20220226&q=ipad"
driver.get(url)
# 清除打开浏览器后自带的 cookies
driver.delete_all_cookies()

# 加载之前保存的 cookies, driver.add_cookie(cookie_dict) 参数是字典对象
with open('./selenium/cookies/taobao_cookies.txt', 'r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)

sleep(1)
driver.get("https://s.taobao.com/search?initiative_id=staobaoz_20220226&q=ipad")

# 打开mysql连接
db_mysql = pymysql.connect(host='localhost',
                     user='root',
                     password='mysql1600',
                     database='taobaoipad')

# 打开mongodb连接
MONGO_URL = 'localhost'
MONGO_DB = 'taobaoipad'
MONGO_COLLECTION = 'taobaoipad'
client = pymongo.MongoClient(MONGO_URL)
db_mongo = client[MONGO_DB]


def index_page(page, db):
    """
        抓取索引页å
    """
    print(f"正在爬取第{page}页")
    try:
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
            input.clear()
            input.send_keys(page)
            submit.click()
        
        # 确定高亮的页面是否是指定的页面
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page)))  # repr(page)
        # 加载商品信息
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1)')))

        get_products(db)

    except TimeoutException:
        index_page(page)


def get_products(db):
    # print("测试")
    # image = driver.find_element_by_css_selector('#J_Itemlist_Pic_667626259158').get_attribute('data-src')
    # print(repr(image))
    """
        提取商品数据
    """
    html = driver.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist > div > div > div:nth-child(1)').children().items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        # print(product)

        save_to_mysql if db == 0 else save_to_mongo


def save_to_mysql(result):
    # 使用cursor()方法获取操作游标 
    cursor = db_mysql.cursor()

    try:
        # SQL 插入语句
        sql = f"""
        INSERT INTO taobaoipad(image, price, deal, title, shop, location)
        VALUES ("{result['image']}", "{result['price']}",  "{result['deal']}",  "{result['title']}",  "{result['shop']}", "{result['location']}")
        """
        
        # 执行sql语句
        cursor.execute(sql)
        # 提交
        db_mysql.commit()
    except Exception:
        print("存储到MySQL失败")

def save_to_mongo(result):
    try:
        db_mongo[MONGO_COLLECTION].insert_one(result)
    except Exception:
        print("存储到MongoDB失败")


if __name__ == '__main__':
    db = int(input("存储到哪个数据库\n0:mysql\n1:mongdo\n"))

    # 读前 20 页数据
    for i in range(1, 21):
        index_page(i, db)

    db_mysql.close()
    driver.quit()

