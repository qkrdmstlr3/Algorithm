"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/3028
"""

import sys

mix = list(sys.stdin.readline().rstrip())
cups = [True, False, False]
for i in mix:
    if i == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif i == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]
print(cups.index(True)+1)
