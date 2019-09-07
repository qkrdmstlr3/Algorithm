"""
    Author : ParkEunsik
    Date   : 2019/09/07
    url    : https://www.acmicpc.net/problem/10866
"""

import sys
from collections import deque

q = deque()

for _ in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_back':
        q.append(order[1])
    elif order[0] == 'push_front':
        q.appendleft(order[1])
    elif order[0] == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
