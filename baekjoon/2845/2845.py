"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2845
"""


import sys

L, P = map(int, sys.stdin.readline().split())

for i in list(map(int, sys.stdin.readline().split())):
    print(i - L*P, end=' ')
