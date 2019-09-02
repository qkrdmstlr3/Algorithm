"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10813
"""

import sys


def minus(num):
    return num-1


N, M = map(int, sys.stdin.readline().split())
basket = list(range(1, N+1))

for _ in range(M):
    i, j = map(minus, map(int, sys.stdin.readline().split()))
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp
print(' '.join(map(str, basket)))
