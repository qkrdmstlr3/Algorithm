"""
    Author : ParkEunsik
    Date   : 2019/07/22
    url    : https://www.acmicpc.net/problem/11279
"""

import sys
import heapq

heap = []
for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
