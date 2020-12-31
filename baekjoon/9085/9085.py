"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/9085
"""

import sys

for i in range(int(sys.stdin.readline())):
    N = sys.stdin.readline()
    num = list(map(int, sys.stdin.readline().split()))
    print(sum(num))
