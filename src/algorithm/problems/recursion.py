import math
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import utils
from utils import __Title__, __print__

__Title__("8.0 모든 순열")
def getSubList(list, subList = []) :
    if len(list) == 0 :
        return subList
    else :
        cur = list[0]
        remain = list[1:]

        has = getSubList(remain, append(subList, cur))
        notHas = getSubList(remain, subList)

        if has != None :
            return has.extend(notHas)
        else :
            return notHas

def append(list, item) :
    copied = list.copy()
    copied.append(item)
    return copied

arrays = ['a', 'b', 'c']
print(getSubList(arrays, []))