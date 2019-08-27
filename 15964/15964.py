"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/15964
"""

import sys

A, B = map(int, sys.stdin.readline().split())
print((A+B)*(A-B))
