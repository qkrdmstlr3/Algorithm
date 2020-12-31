"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/10103
"""

import sys

a, b = 100, 100

for i in range(int(sys.stdin.readline())):
    c, d = map(int, sys.stdin.readline().split())
    if c > d:
        b -= c
    elif c < d:
        a -= d
print(a, b, sep='\n')
