"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2909
"""
import sys

c, k = map(int, sys.stdin.readline().split())

if c % (10**k) == 5:  # 파이썬은 5에서 반올림하면 버림처리됨 > 5에서 반올림 할 때 예외로 처리해주었음
    a = c // (10**k) + 1
    a *= (10**k)
    print(a)
else:
    print(round(c, -k))
