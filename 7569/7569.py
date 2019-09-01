"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/7569
    correct percentage : 36.632%
"""

import sys
from collections import deque

x_plus = [1, -1, 0, 0]
y_plus = [0, 0, -1, 1]
z_plus = [1, -1]
decart = deque()
M, N, H = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(H)]
num_max = 0
for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if tomato[i][j][k] == 1:
                decart.append((i, j, k))
                

def bfs():
    while decart:
        z, x, y = decart.popleft()
        for i in range(4):  # 주변을 고려
            xx = x + x_plus[i]
            yy = y + y_plus[i]
            if xx >= N or xx < 0 or yy >= M or yy < 0:
                continue
            if tomato[z][xx][yy] == 0:
                tomato[z][xx][yy] += tomato[z][x][y]+1
                decart.append((z ,xx, yy))
        for i in range(2):  # 높이를 고려
            zz = z + z_plus[i]
            if zz >= H or zz < 0:
                continue
            if tomato[zz][x][y] == 0:
                tomato[zz][x][y] += tomato[z][x][y]+1
                decart.append((zz ,x, y))
                

bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
            num_max = max(num_max, tomato[i][j][k])
print(num_max-1)
