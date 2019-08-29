"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/7569
    correct percentage: 30.139%
"""

import sys
from collections import deque

decart = deque()
tomato = []
x_plus = [1, -1, 0, 0]
y_plus = [0, 0, -1, 1]
M, N = map(int, sys.stdin.readline().split())
num_max = 0
for i in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            decart.append((i, j))


def dfs():
    while decart:
        x, y = decart.popleft()
        for i in range(4):
            xx = x + x_plus[i]
            yy = y + y_plus[i]
            if xx >= N or xx < 0 or yy >= M or yy < 0:
                continue
            if tomato[xx][yy] == 0:
                tomato[xx][yy] += tomato[x][y]+1
                decart.append((xx, yy))



dfs()
for i in range(N):
    for j in range(M):
        num_max = max(num_max, tomato[i][j])
        if tomato[i][j] == 0:
            print(-1)
            exit()
print(num_max-1)
