"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2501
"""

import sys

N, K = map(int, sys.stdin.readline().split())
cnt, temp = 0, 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        temp = i
        if cnt == K:
            break
if K > cnt:
    print(0)
else:
    print(temp)
