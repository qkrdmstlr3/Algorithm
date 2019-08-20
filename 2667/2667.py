"""
    Author : ParkEunsik
    Date   : 2019/08/20
    url    : https://www.acmicpc.net/problem/2667
    correct percentage: 38.043%
"""

import sys

check_x = [-1, 1, 0, 0]
check_y = [0, 0, -1, 1]
N = int(sys.stdin.readline())
count, house_cnt = 0, []
apart = []


def dfs(i, j):
    global count
    count += 1
    apart[i][j] = '0'
    for k in range(4):
        x = i+check_x[k]
        y = j+check_y[k]
        if x < 0 or x >= N or y < 0 or y >= N:
            continue
        if apart[x][y] == '1':
            dfs(x, y)


for i in range(N):
    apart.append(list(sys.stdin.readline()))

for i in range(N):
    for j in range(N):
        if apart[i][j] == '1':
            count = 0
            dfs(i, j)
            house_cnt.append(count)
house_cnt.sort()
print(len(house_cnt))
for i in range(len(house_cnt)):
    print(house_cnt[i])
