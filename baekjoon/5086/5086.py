"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/5086
"""

import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    elif a == 0 or b == 0:
        print("neither")
        continue
    elif a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
