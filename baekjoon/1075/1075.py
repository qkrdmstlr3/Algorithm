"""
    Author : ParkEunsik
    Date   : 2019/07/31
    url    : https://www.acmicpc.net/problem/1075
"""

import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

N = N // 100 * 100
while N % F != 0:
    N += 1
if N % 100 < 10:
    print(0, N % 100, sep='')
else:
    print(N % 100)
