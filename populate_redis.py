# -*- coding: utf-8 -*-

import redis
import codecs

def populate(redis_host='localhost', redis_port=6379, dict_file='data/dict.txt.big'):
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    f = codecs.open(dict_file, 'r', 'utf-8')
    for l in f.readlines():
        zh, num, pos = l.split(" ")
        r.zadd('words', int(num), zh)
    f.close()

if __name__ == '__main__':
    print("Populating redis...")

    populate()

    print("Redis populated!")