"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2566
"""

import sys

column, row = 0, 0
s_mx = 0
for i in range(9):
    li = list(map(int, sys.stdin.readline().split()))
    if max(li) > s_mx:
        s_mx = max(li)
        column, row = i+1, li.index(max(li))+1
print(s_mx)
print(column, row)
