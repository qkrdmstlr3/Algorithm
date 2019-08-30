"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/2164
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
if N == 1:
    print(1)
elif N <= 3:
    print(2)
else:
    array = deque()
    for i in range(1, N//2+1):
        array.append(i*2)
    if N % 2 != 0:
        array.append(array.popleft())
    while array:
        array.popleft()
        if len(array) == 1:
            print(array[0])
            break
        array.append(array.popleft())
