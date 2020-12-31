"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13417
"""

import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    card = list(sys.stdin.readline().rstrip().split(' '))
    result = deque(card[0])
    for i in range(1, n):
        if result[0] >= card[i]:
            result.appendleft(card[i])
        else:
            result.append(card[i])
    print(''.join(result))
