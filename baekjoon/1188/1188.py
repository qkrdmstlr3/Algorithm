"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1188
    correct percentage : 44.793%
"""

import sys
from fractions import gcd

N, M = map(int, sys.stdin.readline().split())

print(M- gcd(N, M))
