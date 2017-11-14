#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

class RedisServer(object):
    def __init__(self):
        self.cache = redis.Redis(host = 'localhost', port = 6379, db = 0) 
    def __new__(cls,*args, **kwargs):
        return object.__new__(cls, *args, **kwargs)  

    def set(self, key, doc):
        print '-=-=-=-=-=-=-=-='
        print key
        print doc
        print '-=-=-=-=-=-=-=-='
        self.cache.set(key, doc)

    def getInstance(self):
        return self.cache
