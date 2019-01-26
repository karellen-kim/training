import math
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import utils
from utils import __Title__, __print__
import bisect

__Title__("10.1 정렬된 두 배열 정렬된 상태로 병합")
def merge(listA, listB) :
    insertIdx = len(listA) + len(listB) - 1
    aIdx = len(listA) - 1
    bIdx = len(listB) - 1

    listA.extend(0 for i in range(0,len(listB)))
    while bIdx >= 0 :
        if aIdx >= 0 and listA[aIdx] > listB[bIdx] :
            listA[insertIdx] = listA[aIdx]
            aIdx = aIdx - 1
        else :
            listA[insertIdx] = listB[bIdx]
            bIdx = bIdx - 1
        insertIdx = insertIdx - 1
    return listA

listA = [2,4,6,8,10]
listB = [1,3,5,7,9,11]
__print__(listA)
__print__(listB)
__print__(merge(listA, listB))


__Title__("10.9 각 행과 열이 오름차순인 MxN 행렬에서 특정 원소를 찾는 함수")
def findFromMatrix_v1(matrix, value) :
    for rowIdx in range(0, len(matrix)) :
        for colIdx in range(0, len(matrix[0])) :
            if matrix[rowIdx][colIdx] == value :
                return (rowIdx, colIdx)
    return None

def findFromMatrix_v2(matrix, value) :
    for rowIdx in range(0, len(matrix)) :
        idx = bisect.bisect(matrix[rowIdx], value)
        if matrix[rowIdx][idx - 1] == value :
            return (rowIdx, idx - 1)
    return None

def findFromMatrix_v3(matrix, value) :
    return None

matrix = [
    [15,20,40,85],
    [20,35,80,95],
    [30,55,95,105],
    [49,80,100,200],
]

__print__(findFromMatrix_v1(matrix, 55)) # O(MN)
__print__(findFromMatrix_v2(matrix, 55)) # O(MlogN)