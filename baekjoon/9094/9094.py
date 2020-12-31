"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/9094
"""

import sys
import itertools

for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    ab, cnt = list(range(1, N)), 0
    for i in itertools.combinations(ab, 2):
        if (i[0]**2 + i[1]**2 + M) % (i[0]*i[1]) == 0:
            cnt += 1
    print(cnt)
