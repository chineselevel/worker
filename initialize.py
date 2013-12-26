import os

print "Creating data directory..."
if not os.path.exists('data'):
    os.makedirs('data')

print "Downloading jieba dictionary..."
import urllib
urllib.urlretrieve ("https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big", "data/dict.txt.big")

print "Compressing dictionary..."
from compress_dict import compress
compress(original="data/dict.txt.big", compressed="data/dict.compressed.spaces")

print "Initializing redis..."
from populate_redis import populate
redis_host = 'localhost'
redis_port = 6379

print "Putting scores into redis..."
populate(redis_host=redis_host, redis_port=redis_port, dict_file='data/dict.txt.big')
print "Putting ranks into redis..."
populate_ranks(redis_host=redis_host, redis_port=redis_port)

print "Done!"