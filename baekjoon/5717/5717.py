"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/5717
"""
import sys

while True:
    m, f = map(int, sys.stdin.readline().split())
    if m == 0 and f == 0:
        break
    else:
        print(m+f)
