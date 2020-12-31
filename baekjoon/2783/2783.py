"""
    Author : ParkEunsik
    Date   : 2019/08/01
    url    : https://www.acmicpc.net/problem/2783
"""

import sys

X, Y = map(int, sys.stdin.readline().split())
cost = 1000/Y * X
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    cost = min(cost, 1000/b * a)
print('{:0.2f}'.format(cost))
