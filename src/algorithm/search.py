import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils
import math

def binarySearch(list, item) :
    start = 0
    end = len(list) - 1

    while end > start :
        mid = (start + end) // 2
        if item > mid :
            start = mid + 1
        else :
            end = mid
    return start

def __binarySearch(list, item) :
    start = 0
    end = len(list) - 1

    while end > start :
        mid = math.ceil((start + end) / 2)
        if item < mid :
            end = mid - 1
        else :
            start = mid
    return start

list = list(range(0, 10))
utils.__print__(list)
insertIdx = binarySearch(list, 4.5)
utils.__print__(insertIdx)
list.insert(insertIdx, 4.5)
utils.__print__(list)