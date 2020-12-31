"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1735
    correct percentage : 45.265%
"""

import sys
from fractions import gcd

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
bz = a*d + c*b
bm = b*d
gongyaksu = gcd(bz, bm)
print(bz//gongyaksu, bm//gongyaksu)
