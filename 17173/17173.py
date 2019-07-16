"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/17173
"""

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num_sum = []
for i in range(len(num)):
    cnt = 1
    while num[i]*cnt <= N:
        if num[i]*cnt not in num_sum:
            num_sum.append(num[i]*cnt)
        cnt += 1

print(sum(num_sum))
