import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils
import math

utils.__Title__("3.1 배열 한개로 스택 3개 구현")
class FixedSizeStack :
    def __init__(self, size):
        self.list = [0 for i in range(0, size * 3)]
        self.size = size
        self.pointer = [size * 0, size * 1, size * 2]

    def push(self, num, item):
        if self.isFull(num) == False:
            self.list[self.pointer[num]] = item
            self.pointer[num] = self.pointer[num] + 1
        else :
            raise ValueError

    def pop(self, num):
        if self.isEmpty(num) == False:
            value = self.list[self.pointer[num] - 1]
            self.pointer[num] = self.pointer[num] - 1
            return value
        else :
            raise ValueError

    def peek(self, num):
        return self.list[self.pointer[num]]

    def isEmpty(self, num):
        return self.size * num == self.pointer[num]

    def isFull(self, num):
        return self.size * (num + 1) <= self.pointer[num]

fixedSizeStack = FixedSizeStack(3)
fixedSizeStack.push(0, 1)
fixedSizeStack.push(0, 2)
fixedSizeStack.push(0, 3)
fixedSizeStack.push(1, 1)

#fixedSizeStack_v1.push(0, 1) # Error
utils.__print__(fixedSizeStack.pop(0))
utils.__print__(fixedSizeStack.pop(0))
#fixedSizeStack_v1.pop(1) # Error

utils.__Title__("3.2 stack에 O(1)시간 안에 동작하는 min함수 구현")
class MinStack :
    def __init__(self, size):
        self.list = [0 for i in range(0, size)]
        self.top = -1

    def push(self, item):
        if (self.isFull() == False) :
            self.top = self.top + 1
            self.list[self.top] = item
        else :
            raise ValueError

    def sort(self):
        return self._sort(self.list[:(self.top + 1)])

    def _sort(self, list):
        if len(list) <= 1 :
            return list
        else :
            half = math.ceil(len(list) / 2)
            sorted1 = self._sort(list[:half])
            sorted2 = self._sort(list[half:])

            p1 = 0
            p2 = 0
            sorted = []
            while p1 <= len(sorted1) - 1 and p2 <= len(sorted2) - 1 :
                if sorted1[p1] <= sorted2[p2] :
                    sorted.append(sorted1[p1])
                    p1 = p1 + 1
                else :
                    sorted.append(sorted2[p2])
                    p2 = p2 + 1
            sorted.extend(sorted1[p1:])
            sorted.extend(sorted2[p2:])
            return sorted

    def pop(self):
        if (self.isEmpty() == False) :
            value = self.list[self.top]
            self.top = self.top - 1
            return value
        else :
            raise ValueError

    def min(self):
        if self.isEmpty() == False :
            return self.sort()[0]
        else :
            raise ValueError

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return len(self.list) - 1 <= self.top

minStack = MinStack(5)
minStack.push(10)
minStack.push(6)
minStack.push(2)
minStack.push(3)
minStack.push(1)
utils.__print__(minStack.min())
utils.__print__(minStack.pop())
utils.__print__(minStack.min())

utils.__Title__("3.3 일정 크기로 넘어가면 내부적으로 크기를 분리하는 stack")

utils.__Title__("3.4 스택 2개로 큐 하나를 구현")

utils.__Title__("3.5 추가 스택 1개 이외에 추가 buffer 없이 작은 값 순서대로 스택 정렬하는 프로그램")
