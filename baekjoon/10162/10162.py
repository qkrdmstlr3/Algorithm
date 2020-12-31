"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10162
"""

import sys

N = int(sys.stdin.readline())

if N % 10 != 0:
    print(-1)
else:
    a = N//300
    b = N % 300 // 60
    c = N % 300 % 60 // 10
    print(a, b, c)
