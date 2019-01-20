import heapq

minHeap = []
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 10)
heapq.heappush(minHeap, 5)
print(heapq.heappop(minHeap))

maxHeap = []
heapq._heapify_max(maxHeap)
heapq.heappush(maxHeap, 1 * -1)
heapq.heappush(maxHeap, 10 * -1)
heapq.heappush(maxHeap, 5 * -1)
print(heapq.heappop(maxHeap) * -1)

import bisect
list = []
bisect.insort(list, 1)
bisect.insort(list, 10)
bisect.insort(list, 5)
print(list)
print(bisect.bisect_left(list, 3))
print(bisect.bisect_right(list, 15))