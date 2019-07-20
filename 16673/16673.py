"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/16673
"""

import sys

C, K, P = map(int, sys.stdin.readline().split())
s = 0

for i in range(1, C+1):
    s += K*i + P*(i**2)
print(s)
