import json

import requests
from pyquery import PyQuery as pq


class ProxyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaClass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print(f'Succeed in geting proxy {proxy}')
            proxies.append((proxy))

    def crawl_daili66(self, page_count=4):
        """
            get daili66
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = requests.get(url).text
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    # def crawl_proxy360(self):
    #     """get Proxy360"""
    #     start_url = 'http://www/proxy360.cn/Region/China'
    #     print('Crawling', start_url)
    #     html = requests.get(url).text
    #     if html:
    #         doc = pq(html)
    #         lines = doc('div[name="list_proxy_ip"]').items()
    #         for linee in lines:
    #             ip = line.find('.tbBottomLine:nth-child(1)').text()
    #             port = line.find('.tbBottomLine:nth-child(2)').text()
    #             yield ':'.join([ip, port])

















