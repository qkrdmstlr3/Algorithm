"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/3036
"""

import sys
from fractions import Fraction

N = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))

for i in range(1,len(ring)):
    if ring[0] % ring[i] == 0:  # 나누어 떨어질 경우
        print(ring[0]//ring[i], '/', 1, sep='')
    else:
        print(Fraction(ring[0], ring[i]))
