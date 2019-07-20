"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/17283
"""

import sys

L = int(sys.stdin.readline())
R = int(sys.stdin.readline())
L = L * R // 100
height, cnt = 0, 2

while L > 5:
    height += cnt * L
    cnt *= 2
    L = L * R // 100
print(height)
