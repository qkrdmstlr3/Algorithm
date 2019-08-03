"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/5575
"""
import sys

for i in range(3):
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    if f < c:
        if e == 0:
            e = 60
            d -= 1
        e -= 1
        f += 60
        f -= c
    else:
        f -= c
    if e < b:
        d -= 1
        e += 60
        e -= b
    else:
        e -= b
    d -= a
    print(d, e, f)
