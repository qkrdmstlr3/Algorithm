"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/10987
"""

import sys

mo, cnt = ['a', 'e', 'i', 'o', 'u'], 0
for i in sys.stdin.readline():
    if i in mo:
        cnt += 1
print(cnt)
