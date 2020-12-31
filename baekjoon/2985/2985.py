"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2985
"""

import sys

a, b, c = map(int, sys.stdin.readline().split())
if a+b == c:
    print(a, "+", b, "=", c, sep='')
elif a-b == c:
    print(a, "-", b, "=", c, sep='')
elif a*b == c:
    print(a, "*", b, "=", c, sep='')
elif a/b == c:
    print(a, "/", b, "=", c, sep='')
elif a == b and b == c:
    print(a, "=", b, "=", c, sep='')
elif a == b - c:
    print(a, "=", b, "-", c, sep='')
elif a == b * c:
    print(a, "=", b, "*", c, sep='')
elif a == b / c:
    print(a, "=", b, "/", c, sep='')
elif a == b + c:
    print(a, "=", b, "+", c, sep='')
