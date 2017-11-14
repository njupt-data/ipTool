# encoding=utf-8

import scrapy
from scrapy import Selector
from spiderIp.items import XICIDAILI


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = 'http://www.xicidaili.com'
    base_address = 'http://www.xicidaili.com/nn/'
    start_urls = []

    def __init__(self):
        self.setUrls(1)

    def setUrls(self, limit):
        for i in range(limit):
            self.start_urls.append(self.base_address + str(i + 1))

    def parse(self, response):
        i = 0
        for tr in response.xpath('//tr'):
            if i > 0:
                yield {
                    'ip': tr.xpath('.//td[2]/text()').extract_first(),
                    'port': tr.xpath('.//td[3]/text()').extract_first(),
                    'address': unicode.encode(tr.xpath('.//td[4]/text()').extract_first(), "utf-8"),
                    'ipType': tr.xpath('.//td[6]/text()').extract_first().encode("utf-8"),
                    'speed': tr.xpath(".//td[7]//div[@class='bar']/@title").extract_first().encode("utf-8"),
                    'linkTime': tr.xpath(".//td[8]//div[@class='bar']/@title").extract_first().encode("utf-8"),
                    'aliveTime': unicode.encode(tr.xpath(".//td[8]//div[@class='bar']/@title").extract_first(), "utf-8"),
                    'verifyTime': tr.xpath(".//td[9]/text()").extract_first().encode("utf-8"),
                }
            i = i + 1
