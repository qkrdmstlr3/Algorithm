"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/2480
"""

import sys

a, b, c = map(int, sys.stdin.readline().split())
if a == b and b == c:
    print(10000+a*1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000+a*100)
    else:
        print(1000+c*100)
else:
    print(100*max(max(a, b), c))
