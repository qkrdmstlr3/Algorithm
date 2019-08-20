"""
    Author : ParkEunsik
    Date   : 2019/08/20
    url    : https://www.acmicpc.net/problem/3184
"""

import sys
sys.setrecursionlimit(100000)  # 최대 재귀할수 있는 범위를 늘려줌(기본 1000)

check_x = [-1, 1, 0, 0]
check_y = [0, 0, -1, 1]
R, C = map(int, sys.stdin.readline().split())
field = []
sheep, wolf = 0, 0
result = [0, 0]


def dfs(i, j):
    global sheep, wolf
    if field[i][j] == 'v':
        wolf += 1
    elif field[i][j] == 'o':
        sheep += 1
    field[i][j] = '#'
    for k in range(4):
        x = i+check_x[k]
        y = j+check_y[k]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if field[x][y] != '#':
            dfs(x, y)


for i in range(R):
    field.append(list(sys.stdin.readline()))
    
for i in range(R):
    for j in range(C):
        if field[i][j] != '#':
            sheep, wolf = 0, 0
            dfs(i, j)
            if sheep > wolf:
                result[0] += sheep
            else:
                result[1] += wolf
print(result[0], result[1])
