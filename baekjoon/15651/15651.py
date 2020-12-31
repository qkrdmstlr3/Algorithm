"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/15651
"""

import sys
from itertools import combinations_with_replacement
from itertools import product

N, M = map(int, sys.stdin.readline().split())
for i in product(list(range(1, N+1)), repeat=M):
    print(' '.join(map(str, i)))
