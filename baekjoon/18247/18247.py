"""
    Author : ParkEunsik
    Date   : 2020/01/05
    url    : https://www.acmicpc.net/problem/18247
"""

import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split(' '));
    if n<12 or m<4:
        print(-1)
        continue
    print(11*m+4)
