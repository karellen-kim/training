import utils

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
            value = self.list[self.pointer[num]]
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

#fixedSizeStack.push(0, 1) # Error
fixedSizeStack.pop(1)
#fixedSizeStack.pop(1) # Error

utils.__Title__("3.2 stack에 O(1)시간 안에 동작하는 min함수 구현")

utils.__Title__("3.3 일정 크기로 넘어가면 내부적으로 크기를 분리하는 stack")

utils.__Title__("3.4 스택 2개로 큐 하나를 구현")

utils.__Title__("3.5 추가 스택 1개 이외에 추가 buffer 없이 작은 값 순서대로 스택 정렬하는 프로그램")