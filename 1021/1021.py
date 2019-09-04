"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1021
"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
dq = deque(list(range(1, N+1)))
count = 0

for i in num:
    index = dq.index(i)
    left = index
    right = len(dq) - index
    if left <= right:
        count += left
        dq.rotate(-left)
        dq.popleft()
    else:
        count += right
        dq.rotate(right)
        dq.popleft()
print(count)
