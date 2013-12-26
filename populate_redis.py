# -*- coding: utf-8 -*-

import redis
import codecs

def populate(redis_host='localhost', redis_port=6379, dict_file='data/dict.txt.big'):
    """
    Takes data from a space-delimited dictionary file with word counts and puts it into
    a sorted redis collection called "words".
    """
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    f = codecs.open(dict_file, 'r', 'utf-8')
    for l in f.readlines():
        zh, num, pos = l.split(" ")
        r.zadd('words', int(num), zh)
    f.close()

def populate_ranks(redis_host='localhost', redis_port=6379):
    """
    Takes data from the words sorted collection and puts it into the ranks sorted collection
    called "ranks".
    """
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
    for i, zh in enumerate(r.zrevrange('words', 0, -1)):
        r.zadd('ranks', i, zh)

if __name__ == '__main__':
    print("Populating redis...")

    populate()

    print("Redis populated!")