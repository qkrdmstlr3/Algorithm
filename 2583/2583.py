"""
    Author : ParkEunsik
    Date   : 2019/09/09
    url    : https://www.acmicpc.net/problem/2583
"""

import sys
sys.setrecursionlimit(100000)

m, n, k = map(int, sys.stdin.readline().split())
paper = [[False]*(n) for _ in range(m)]
count = 0
x_plus = (1, -1, 0, 0)
y_plus = (0, 0, 1, -1)

for _ in range(k):
    coor = list(map(int, sys.stdin.readline().split()))
    for i in range(coor[0], coor[2]):
        for j in range(coor[1], coor[3]):
            paper[j][i] = True
    
def dfs(x, y):
    global count
    if paper[x][y] is True:
        return
    paper[x][y] = True
    count += 1
    for i in range(4):
        xx = x + x_plus[i]
        yy = y + y_plus[i]
        if xx >= m or xx < 0 or yy >= n or yy < 0:
            continue
        dfs(xx, yy)

area = []
for i in range(m):
    for j in range(n):
        if paper[i][j] is False:  # 종이인 부분
            dfs(i, j)
            area.append(count)
            count = 0
print(len(area))
print(' '.join(map(str, sorted(area))))
