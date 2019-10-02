"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/10865
"""

import sys

n, m = map(int, sys.stdin.readline().split())
friend = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend[a] += 1
    friend[b] += 1
for i in range(1, n+1):
    print(friend[i])
    