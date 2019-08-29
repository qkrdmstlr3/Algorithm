"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/4101
"""

import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print("Yes") if a > b else print("No")
