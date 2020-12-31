"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2525
"""

import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

hour = C // 60
minute = C % 60

if B+minute >= 60:
    A += 1
    print((A+hour)%24, B+minute-60)
else:
    print((A+hour)%24, B+minute)
