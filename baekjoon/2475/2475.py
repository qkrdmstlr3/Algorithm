"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/2475
"""

import sys

num = list(map(int, sys.stdin.readline().split()))
sm = 0
for i in range(len(num)):
    sm += (num[i] % 10)**2
print(sm % 10)
