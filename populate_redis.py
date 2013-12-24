# -*- coding: utf-8 -*-

import redis
import codecs

redis_host = 'localhost'
redis_port = 6379

r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

if __name__ == '__main__':
    print("Populating redis...")

    f = codecs.open('data/dict.txt.big', 'r', 'utf-8')
    for l in f.readlines():
        zh, num, pos = l.split(" ")
        r.zadd('words', int(num), zh)

    print("Redis populated!")