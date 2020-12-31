"""
    Author : ParkEunsik
    Date   : 2019/07/17
    url    : https://www.acmicpc.net/problem/2869
    correct percentage : 30.162%
    이전 날의 높이를 구해서 계산
"""

import sys

A, B, V = map(int, sys.stdin.readline().split())
t, f = V-A-1, A-B
print((t+f-(t % f))//f + 1)
