"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2495
"""

import sys

for j in range(3):
    N, cnt, mx = sys.stdin.readline(), 1, 1
    for i in range(len(N)-2):
        if N[i] == N[i+1]:
            cnt += 1
        else:
            cnt = 1
        if mx < cnt:
                mx = cnt
    print(mx)
