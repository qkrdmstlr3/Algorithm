"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/15650
"""

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
li = list(range(1, N+1))
for i in itertools.combinations(li, M):
    print(" ".join(map(str, i)))
