"""
    Author : ParkEunsik
    Date   : 2019/08/15
    url    : https://www.acmicpc.net/problem/15649
"""

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
li = list(range(1, N+1))
for i in itertools.permutations(li, M):
    print(' '.join(map(str, i)))

