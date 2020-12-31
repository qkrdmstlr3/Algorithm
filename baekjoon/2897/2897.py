"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/2897
"""

import sys

row, column = map(int, sys.stdin.readline().split())

park, cnt = [], [0, 0, 0, 0, 0]
for i in range(row):
    park.append(sys.stdin.readline())

for i in range(row-1):
    for j in range(column-1):
        place = 0
        if park[i][j] == '#' or park[i+1][j] == '#' or park[i][j+1] == '#' or park[i+1][j+1] == '#':
            continue
        if park[i][j] == 'X':
            place += 1
        if park[i+1][j] == 'X':
            place += 1
        if park[i][j+1] == 'X':
            place += 1
        if park[i+1][j+1] == 'X':
            place += 1
        cnt[place] += 1
for i in range(5):
    print(cnt[i])
