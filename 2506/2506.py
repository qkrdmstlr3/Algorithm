"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/2506
"""

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
cnt, s = 1, 0
for i in range(len(num)):
    if num[i] == 0:
        cnt = 1
    else:
        s += cnt
        cnt += 1
print(s)
