from myRedis import RedisClient
from getProxy import Crawler

POOL_UPPER_THRESHOLD = 10000


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """confirm not beyond the upper threshold"""
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('getter start running')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                if proxies:
                    for proxy in proxies:
                        self.redis.add(proxy)
