import redis
from random import choice
from error import PoolEmeptyError

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_KEYWORD = None
REDIS_KEY = 'proxies'


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_KEYWORD):
        """
            Initialize proxies
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
            Add proxies and set score to INITIAL_SCORE(100)
            :return: the number of added agent
        """
        if not self.db.zscore(REDIS_KEY, proxy):  # proxy not in redis
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        """
            Get valid proxy at random, first try to get the highest score proxy, if not exists, get proxy by ranking.
            :return: random proxy 
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)

        else:
            result = self.db.zrevrange(REDIS_KEY, MIN_SCORE, MAX_SCORE)
            if len(result):
                return choice(result)
            else:
                raise PoolEmeptyError

    def decrease(self, proxy):
        """
            the score of proxy decrease 1, if the score less than MIN_SCORE, leave out the proxy.
            :return: decreased score 
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print(f"proxy: {proxy}, now score: {score}, decrease 1")
            return self.db.zincrby(REDIS_KEY, proxy, -1)

        else:
            print(f"proxy: {proxy}, now score: {score}, leave out")
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """return true if proxy is existing"""
        return not self.db.zscore(REDIS_KEY, proxy) is None

    def max(self, proxy):
        """set the score of proxy to MAX_SCORE"""
        print(f"proxy: {proxy}, set score to {MAX_SCORE}")
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """get the number of proxies """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """get all proxies"""
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
