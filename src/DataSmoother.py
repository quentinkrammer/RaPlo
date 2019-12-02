# -*- coding: utf-8 -*-
import collections
import statistics

class DataSmoother(object):

    def __init__(self, length=5):
        self.piorData = collections.deque([], length)
        
    def __call__(self, data):
        mean = statistics.mean(data)         
        self.piorData.append(mean)        
        median = statistics.median(self.piorData)
        return median
        