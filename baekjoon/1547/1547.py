"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/1547
"""

import sys

cup = [0]*4
cup[1] = 1
for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    temp = cup[x]
    cup[x] = cup[y]
    cup[y] = temp
print(cup.index(1))
