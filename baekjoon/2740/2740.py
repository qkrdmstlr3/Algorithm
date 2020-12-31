"""
    Author : ParkEunsik
    Date   : 2019/09/15
    url    : https://www.acmicpc.net/problem/2740
"""

import sys
import numpy as np

n, m = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
p, k = map(int, sys.stdin.readline().split())
b = []
for _ in range(p):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(k):
        s = 0
        for n in range(m):
            s += a[i][n] * b[n][j]
        print(s, end=' ')
    print()
