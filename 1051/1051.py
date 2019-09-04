"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1051
    correct percentage : 36.681%
"""

import sys

N, M = map(int, sys.stdin.readline().split())
square = []
num_max = 0
for _ in range(N):
    square.append(list(sys.stdin.readline().rstrip()))
for i in range(1, min(N, M)):  # 1 2
    for j in range(N):
        for k in range(M):
            if j+i >= N or k+i >= M:
                continue
            if square[j][k] == square[j][k+i] and square[j][k] == square[j+i][k] and square[j][k] == square[j+i][k+i]:
                num_max = max(num_max, i)
print((num_max+1)**2)
