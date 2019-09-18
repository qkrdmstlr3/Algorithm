"""
    Author : ParkEunsik
    Date   : 2019/09/18
    url    : https://www.acmicpc.net/problem/1247
    correct percentage : 40.157%
"""

import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    num = []
    for _ in range(N):
        num.append(int(sys.stdin.readline()))
    if sum(num) > 0:
        print("+")
    elif sum(num) < 0:
        print("-")
    else:
        print("0")
