"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/10156
"""

import sys

k, n, m = map(int, sys.stdin.readline().split())
if 0 >= k*n-m:
    print(0)
else:
    print(k*n-m)
