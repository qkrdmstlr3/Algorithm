"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/17356
"""

import sys

A, B = map(int, sys.stdin.readline().split())
M = (B-A)/400

print(1/(1+10**M))
