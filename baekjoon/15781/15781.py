"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/15781
"""

import sys

N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
h.sort()
a.sort()
print(h[-1]+a[-1])
