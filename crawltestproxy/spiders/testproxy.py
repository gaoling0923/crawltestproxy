# -*- coding: utf-8 -*-
import scrapy


class TestproxySpider(scrapy.Spider):
    name = 'testproxy'
    allowed_domains = ['ip.filefab.com']
    start_urls = ['http://ip.filefab.com/index.php']

    def parse(self, response):
        # cc2=response.css('#ipd  span:text').extract_first()
        print(response.text)

