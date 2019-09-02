"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/15652
"""

import sys
from itertools import combinations_with_replacement
from itertools import product

N, M = map(int, sys.stdin.readline().split())
for i in combinations_with_replacement(list(range(1, N+1)), M):
    print(' '.join(map(str, i)))

