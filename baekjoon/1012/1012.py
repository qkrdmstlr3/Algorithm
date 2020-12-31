"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/1012
"""

import sys
from collections import deque

sys.setrecursionlimit(100000) 

x_plus = (1, -1, 0, 0)
y_plus = (0, 0, 1, -1)


def dfs(x, y):
    bat[x][y] = 0
    for i in range(4):
        xx = x+x_plus[i]
        yy = y+y_plus[i]
        if xx >= N or xx < 0 or yy >= M or yy < 0:
            continue
        if bat[xx][yy] == 1:
            dfs(xx, yy)


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    count = 0
    bat = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bat[y][x] = 1
    for i in range(N):
        for j in range(M):
            if bat[i][j]:
                count += 1
                dfs(i, j)
    print(count)
