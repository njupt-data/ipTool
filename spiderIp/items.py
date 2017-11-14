# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class XICIDAILI(scrapy.Item):
	# ip地址
	ip = scrapy.Field()
	# 端口号
	port = scrapy.Field()
	# 省份地区
	address = scrapy.Field()
	# HTTP or HTTPs
	ipType = scrapy.Field()
	# 链接速度
	speed = scrapy.Field()
	# 连接时间
	linkTime = scrapy.Field()
	# 存活时间
	aliveTime = scrapy.Field()
	# 验证时间
	verifyTime = scrapy.Field()