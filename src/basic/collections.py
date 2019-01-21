import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils

utils.__Title__("리스트 : 스택")
## 리스트
## 리스트 : 스택
s = []
s.append(1)
s.append(2)
s.append(3)
utils.__print__(s)
utils.__print__(s.pop())
utils.__print__(s.pop())
utils.__print__(s)

utils.__Title__("리스트 : 큐")
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
utils.__print__(q)
utils.__print__(q.popleft())
utils.__print__(q.pop())
utils.__print__(q)

utils.__Title__("비동기 큐")
import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
utils.__print__(q.get())
utils.__print__(q.get())

