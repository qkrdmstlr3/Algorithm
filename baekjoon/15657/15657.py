"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/15657
"""

import sys
from itertools import combinations_with_replacement
from itertools import product

N, M = map(int, sys.stdin.readline().split())
array = sorted(list(map(int, sys.stdin.readline().split())))
for i in combinations_with_replacement(array, M):
    print(' '.join(map(str, i)))
