"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1551
"""

import sys

N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split(',')))

for _ in range(K):
    for i in range(len(a)-1):
        a[i] = a[i+1]-a[i]
    a.pop()
print(','.join(map(str, a)))
