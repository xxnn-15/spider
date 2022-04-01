import asyncio
import time
from myRedis import  RedisClient

import aiohttp
VALID_STATUS_CODE = [200]
TEST_URL = 'https://www.baidu.com'
BATCH_TEST_SIZE = 100


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self, proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print(f'Testing: {proxy}')
                async with session.get(TEST_URL, proxy=real_proxy, async_timeout=15) as response:
                    if response.status in VALID_STATUS_CODE:
                        self.redis.max(proxy)
                        print(f'proxy available: {proxy}')
                    else:
                        self.redis.decrease(proxy)
                        print(f'the status code is invalid: {proxy}')
            except:
                self.redis.decrease(proxy)
                print(f'proxy request failed: {proxy}')

    def run(self):
        """Test moudle main function"""
        print('Test starts executing')
        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop()

            for i in range(0, len(proxies), BATCH_TEST_SIZE):
                test_proxies = proxies[i:i + BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run.until_complete(asyncio.wait(tasks))
                time.sleep(5)

        except Exception as e:
            print('Test moudle error', e.args)

