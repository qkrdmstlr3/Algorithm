"""
    Author : ParkEunsik
    Date   : 2019/07/25
    url    : https://www.acmicpc.net/problem/2460
"""

import sys

mx, pas = 0, 0
for i in range(10):
    d, u = map(int, sys.stdin.readline().split())
    pas -= d
    pas += u
    mx = max(mx, pas)
print(mx)
