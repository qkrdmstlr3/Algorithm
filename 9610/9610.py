"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/9610
"""

import sys

result = [0, 0, 0, 0, 0]
for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        result[4] += 1
    elif x > 0 and y > 0:
        result[0] += 1
    elif x < 0 and y > 0:
        result[1] += 1
    elif x < 0 and y < 0:
        result[2] += 1
    elif x > 0 and y < 0:
        result[3] += 1
for i in range(1, 5):
    print("Q", i, ": ", result[i-1], sep='')
print("AXIS: ", result[4], sep='')
