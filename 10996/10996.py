"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/10996
"""

import sys

N = int(sys.stdin.readline())

if N == 1:
    print('*')
else:
    if N % 2 == 0:
        for i in range(N):
            print('* '*(N//2))
            print(' *'*(N//2))
    else:
        for i in range(N):
            print('* '*(N//2+1))
            print(' *'*(N//2))
