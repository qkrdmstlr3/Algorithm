"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/2178
    correct percentage : 34.111%
"""

import sys
from collections import deque

x_plus = (1, -1, 0, 0)
y_plus = (0, 0, 1, -1)
N, M = map(int, sys.stdin.readline().split())
miro = []
road = deque()
num_max = 0
road.append((0, 0))
for i in range(N):
    miro.append(list(map(int, list(sys.stdin.readline().rstrip()))))


def bfs():
    while road:
        x, y = road.popleft()
        for i in range(4):
            xx = x + x_plus[i]
            yy = y + y_plus[i]
            if xx >= N or xx < 0 or yy >= M or yy < 0:
                continue
            if miro[xx][yy] == 1:
                miro[xx][yy] += miro[x][y]
                road.append((xx, yy))


bfs()
print(miro[N-1][M-1])
