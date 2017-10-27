# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from scrapy import signals
from scrapy.conf import settings
import random

# from crawAutohomebbsdetail.dbpackage.dbresdis import RedisClient
from selenium.webdriver.common.proxy import ProxyType


class proxMiddleware(object):
    proxy_list=[
        "http://119.28.136.72:3128",
     "http://176.104.196.234:8081"
     "http://176.104.196.234:8081"
     "http://176.104.196.234:8081"
     "http://176.104.196.234:8081"
     "http://200.48.129.123:8080"]

    def process_request(self, request, spider):
        # if not request.meta['proxies']:
        ip = random.choice(self.proxy_list)
        ip = self.get_proxy()
        print(ip)
        # print 'ip=' %ip
        request.meta['proxy'] = ip
    def get_proxy(self):
        try:
            response = requests.get(settings['PROXY_POOL_URL'])
            if response.status_code == 200:

                return response.text
            return None
        except ConnectionError:
            return None
class JavaScriptProxyMiddleware(object):

    def process_request(self, request, spider):
        # conn = RedisClient();
        # proxy = conn.pop();
        # print('当前使用的IP:', proxy);
        # request.meta['proxy'] = "http://%s" % proxy

        # proxy=self.get_proxy()
        if spider.name in("testproxy"):
            print("execute PhantomJS spiderName", spider.name);
            print("PhantomJS is starting...")
            driver = webdriver.PhantomJS() #指定使用的浏览器
            #driver =webdriver.Chrome()
            # driver = webdriver.Firefox()
            # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
            proxy = webdriver.Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxyip=self.get_proxy()
            print('PROXY_IP:', proxyip)

            if proxyip:
                print('进入:', proxyip)
                proxy.http_proxy = proxyip

                # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
                proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
                driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
                driver.get(request.url)
                print('1: ', driver.session_id)
                # print('2: ', driver.page_source)
                print('3: ', driver.get_cookies())
                #driver.p
                # js = "var q=document.documentElement.scrollTop=10000"
                # browser.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
                # time.sleep(3)
                body = driver.page_source
                # print ("访问2="+body)
                print ("访问="+request.url)
                return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
            else:
                proxy = webdriver.Proxy()
                proxy.proxy_type = ProxyType.DIRECT
                proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
                driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
                return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

        else:
            return

    def get_proxy(self):
        try:
            response = requests.get(settings['PROXY_POOL_URL'])
            if response.status_code == 200:

                return response.text
            return None
        except ConnectionError:
            return None
class JavaScriptMiddleware(object):

    def process_request(self, request, spider):
        # conn = RedisClient();
        # cproxy = conn.pop();
        # print('当前使用的IP:', cproxy);
        # request.meta['proxy'] = "http://%s" % proxy

        if spider.name in("spiderbbs","crawlb30bbsdetail"):
            print("execute PhantomJS spiderName", spider.name);
            print("PhantomJS is starting...")
            driver = webdriver.PhantomJS() #指定使用的浏览器
            driver.get(request.url)
            # driver.get
            #driver.p
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(3)
            body = driver.page_source
            print ("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return
class CrawltestproxySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
