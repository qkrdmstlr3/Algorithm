"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/11286
    우선순위 큐 > heap
"""

import sys
import heapq

li = []
heap = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))
