"""
    Author : ParkEunsik
    Date   : 2019/07/31
    url    : https://www.acmicpc.net/problem/10539
"""

import sys

N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    B[i] = B[i]*(i+1)
for i in range(len(B)):
    B[i] -= sum(B[:i])
    print(B[i], end=' ')
