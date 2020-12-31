"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/10822
"""

import sys

li, s = list(map(int, sys.stdin.readline().split(','))), 0

for i in range(len(li)):
    s += li[i]
print(s)
