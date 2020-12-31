"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/9546
"""

import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    num = 0
    for _ in range(k):
        num = (num + 0.5) * 2;
    print(int(num))
