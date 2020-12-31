"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/17009
"""

import sys

s1, s2 = 0, 0
for a in reversed(range(1, 4)):
    s1 += a * int(sys.stdin.readline())
for a in reversed(range(1, 4)):
    s2 += a * int(sys.stdin.readline())
if s1 > s2:
    print("A")
elif s1 < s2:
    print("B")
else:
    print("T")
