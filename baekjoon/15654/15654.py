"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/15654
"""

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

for i in itertools.permutations(num, M):
    print(' '.join(map(str, i)))
