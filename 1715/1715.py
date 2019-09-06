"""
    Author : ParkEunsik
    Date   : 2019/09/06
    url    : https://www.acmicpc.net/problem/1715
    correct percentage : 38.621%
    heap
"""

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
final_count = 0
for _ in range(N):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)
for i in range(0, (N-1)*2, 2):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    final_count += a+b
    heapq.heappush(heap, a+b)
print(final_count)
