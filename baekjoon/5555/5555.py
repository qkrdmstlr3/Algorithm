"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/5555
"""

import sys

text, cnt = input(), 0
for i in range(int(sys.stdin.readline())):
    ring = input()
    ring += ring[:len(text)]
    if text in ring:
        cnt += 1
print(cnt)
