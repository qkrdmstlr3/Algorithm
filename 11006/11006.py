"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/11006
"""

import sys

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    index = 0
    if N == M:
        print(N, 0)
    else:
        while N // M != 2:
            index += 1
            N -= 1
            M -= 1
        print(index, M)
