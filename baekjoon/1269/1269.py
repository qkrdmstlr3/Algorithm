"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1269
    correct percentage : 48.840%
"""

import sys

A, B = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

C = (A-B)|(B-A)
print(len(C))
