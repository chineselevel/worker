import codecs
import json
import math
from collections import defaultdict

def compress(original="data/dict.txt.big", compressed="data/dict.compressed.tab"):
    f = codecs.open(original, "r", "utf-8")
    w = codecs.open(compressed, 'w', 'utf8')

    words = []

    # zipf's law parameters (not used right now):
    N = 0  # total number of words
    s = 1.0  # the value of the exponent characterizing the distribution.
    q = 2.0  # variable characterizing the distribution

    total_words = 0

    for i, line in enumerate(f.readlines()):
        l = map(unicode.strip, line.split(' '))
        words.append((l[0], int(l[1]), l[2]))
        total_words += int(l[1])
        N += 1

    words = sorted(words, key=lambda w: w[1], reverse=True)

    normalizer = sum([1 / math.pow(n + q, s) for n in range(1, N+1)])
    diff = 0

    for k, word in enumerate(words):
        w.write(u"{}\n".format(word[0], word[2]))

    f.close()
    w.close()

if __name__ == '__main__':
    print "Compressing dict..."
    compress()
    print "Done!"