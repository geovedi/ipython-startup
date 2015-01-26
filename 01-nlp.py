# -*- coding: utf-8 -*-

# http://stackoverflow.com/a/7595897
def gen_ngrams(tokens, MIN_N, MAX_N):
    n_tokens = len(tokens)
    for i in xrange(n_tokens):
        for j in xrange(i+MIN_N, min(n_tokens, i+MAX_N)+1):
            yield tokens[i:j]

from itertools import combinations
# find all possible ordered phrases - http://stackoverflow.com/a/18406982
def find_combo(tokens):
    ns = range(1, len(tokens))
    for n in ns:
        for ix in combinations(ns, n):
            yield [' '.join(tokens[i:j]) for i, j in zip((0,)+ix, ix+(None,))]


# http://stackoverflow.com/a/699892
def int2bin(i):
    return '{0:b}'.format(i)


def bin2int(b):
    return int(b[::-1], 2)


