"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/10773
"""

import sys

li = []
for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N == 0:
        li.pop()
    else:
        li.append(N)
print(sum(li))
