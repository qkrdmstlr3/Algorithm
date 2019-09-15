"""
    Author : ParkEunsik
    Date   : 2019/09/15
    url    : https://www.acmicpc.net/problem/2589
    correct percentage: 39.937%
"""

import sys
from collections import deque
sys.setrecursionlimit(100000)

check_x = (-1, 1, 0, 0)
check_y = (0, 0, -1, 1)
L, W = map(int, sys.stdin.readline().split())
treasure = []
max_distance, count = 0, 0
for i in range(L):
    treasure.append(sys.stdin.readline().rstrip())


def bfs(x, y, count):
    q = deque()
    q.append([x, y, count])
    max_count = 0
    copy_check[x][y] = True
    while q:
        xx, yy , ccount = q.popleft()
        for i in range(4):
            xxx = xx + check_x[i]
            yyy = yy + check_y[i]
            if xxx >= L or xxx < 0 or yyy >= W or yyy < 0:
                continue
            if copy_check[xxx][yyy] is False and treasure[xxx][yyy] == 'L':  # Boolean배열과 기존 입력받은 배열을 같이 체크
                copy_check[xxx][yyy] = True
                max_count = max(max_count, ccount+1)
                q.append([xxx, yyy, ccount+1])
    return max_count


for i in range(L):
    for j in range(W):
        if treasure[i][j] == 'L':
            count = 0
            copy_check = [[False]*W for _ in range(L)]
            max_distance = max(max_distance, bfs(i, j, count))
print(max_distance)
