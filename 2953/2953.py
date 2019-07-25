"""
    Author : ParkEunsik
    Date   : 2019/07/25
    url    : https://www.acmicpc.net/problem/2953
"""

import sys

mx, index = 0, 0
for i in range(1, 6):
    s = sum(list(map(int, sys.stdin.readline().split())))
    if s > mx:
        mx = s
        index = i
print(index, mx)
