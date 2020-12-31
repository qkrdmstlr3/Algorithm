"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/10250
    correct percentage : 35.956%
"""

import sys

for i in range(int(sys.stdin.readline())):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H == 0:  # 꼭대기 층
        column = H
        row = N // H
    else:
        column = N % H
        row = N // H + 1
    print(100*column + row)
