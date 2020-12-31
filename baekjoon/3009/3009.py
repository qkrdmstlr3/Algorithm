"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/3009
"""

import sys

x, y = [0], [0]
x[0], y[0] = map(int, sys.stdin.readline().split())
for i in range(2):
    c, d = map(int, sys.stdin.readline().split())
    if c in x:
        x.remove(c)
    else:
        x.append(c)
    if d in y:
        y.remove(d)
    else:
        y.append(d)
print(x[0], y[0])
