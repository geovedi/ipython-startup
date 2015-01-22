# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from random import Random

# stolen from @ogrisel Parallel ML tutorial
class InfiniteStreamGenerator(object):
    """Simulate random polarity queries on the twitter streaming API"""
    
    def __init__(self, texts, targets, seed=0, batchsize=100):
        self.texts_pos = [text for text, target in zip(texts, targets)
                               if target > 2]
        self.texts_neg = [text for text, target in zip(texts, targets)
                               if target <= 2]
        self.rng = Random(seed)
        self.batchsize = batchsize

    def next_batch(self, batchsize=None):
        batchsize = self.batchsize if batchsize is None else batchsize
        texts, targets = [], []
        for i in range(batchsize):
            # Select the polarity randomly
            target = self.rng.choice((0, 4))
            targets.append(target)
            
            # Combine 2 random texts of the right polarity
            pool = self.texts_pos if target > 2 else self.texts_neg
            text = self.rng.choice(pool) + " " + self.rng.choice(pool)
            texts.append(text)
        return texts, targets

