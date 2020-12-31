"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/1568
"""

import sys

N = int(sys.stdin.readline())

time = 0
cnt = 1
while N > 0:
    N -= cnt
    time += 1
    cnt += 1
    if N < cnt:
        cnt = 1
print(time)
