"""
    Author : ParkEunsik
    Date   : 2019/09/09
    url    : https://www.acmicpc.net/problem/1743
"""

import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, sys.stdin.readline().split())
road = [[False]*m for _ in range(n)]
num_max = 0
x_plus = (1, -1, 0, 0)
y_plus = (0, 0, 1, -1)
count = 0

for _ in range(k):
    r, c = map(lambda x: x-1, map(int, sys.stdin.readline().split()))
    road[r][c] = True

def dfs(x, y):
    global count
    if road[x][y] is False:
        return
    road[x][y] = False
    count += 1
    for i in range(4):
        xx = x + x_plus[i]
        yy = y + y_plus[i]
        if xx >= n or xx < 0 or yy >= m or yy < 0:
            continue
        dfs(xx, yy)

for i in range(n):
    for j in range(m):
        if road[i][j] is True:
            dfs(i, j)
            num_max = max(num_max, count)
            count = 0
print(num_max)
