"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13410
"""

import sys

n, k = map(int, sys.stdin.readline().split())

max_num = 0

for i in range(1, k+1):
    num = int(''.join(reversed(str(n*i))))
    max_num = max(max_num, num)
print(max_num)
