# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from redisServer import RedisServer

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.redis = RedisServer()
        # self.file = codecs.open('items.json', 'wb', encoding='utf-8')

    def process_item(self, dt, spider):
        self.redis.set('ip', dt)
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line.decode('unicode_escape'))
        return dt
