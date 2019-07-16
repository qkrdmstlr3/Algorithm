"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/17174
"""

import sys

N, M = map(int, sys.stdin.readline().split())

sum = 0
while N > 0:
    sum += N
    N //= M
print(sum)
