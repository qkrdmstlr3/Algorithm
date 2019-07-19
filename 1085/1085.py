"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/1085
"""

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

row = min(x, w-x)
column = min(y, h-y)
print(min(row, column))
