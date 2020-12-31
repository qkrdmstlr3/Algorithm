"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/10819
"""

import sys
import itertools

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
mx = 0

for i in itertools.permutations(A, N):
    s = 0
    for j in range(N-1):
        s += abs(i[j]-i[j+1])
    mx = max(mx, s)
print(mx)
