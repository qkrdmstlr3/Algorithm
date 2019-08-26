"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2530
"""

import sys

A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

hour = D//3600
minute = (D-hour*3600)//60
second = D%60

if C+second >= 60:
    B += 1
    if B+minute >= 60:
        A += 1
        print((A+hour)%24, B+minute-60, C+second-60)
    else:
        print((A+hour)%24, B+minute, C+second-60)
else:
    if B+minute >= 60:
        A += 1
        print((A+hour)%24, B+minute-60, C+second)
    else:
        print((A+hour)%24, B+minute, C+second)
