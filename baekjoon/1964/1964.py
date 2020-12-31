"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/1964
"""

import sys

N = int(sys.stdin.readline())
print((1 + 4*N + 3*N*(N-1)//2) % 45678)
