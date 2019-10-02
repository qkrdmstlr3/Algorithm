"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/10864
"""

import sys

n, m = map(int, sys.stdin.readline().split())
friend = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b not in friend[a]:
        friend[a].append(b)
    if a not in friend[b]:
        friend[b].append(a)
for i in range(1, n+1):
    print(len(friend[i]))
    