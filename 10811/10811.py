"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10811
"""

import sys


def minus(num):
    return num-1


N, M = map(int, sys.stdin.readline().split())
basket = list(range(1, N+1))
for _ in range(M):
    i, j = map(minus, map(int, sys.stdin.readline().split()))
    basket = basket[:i]+list(reversed(basket[i:j+1]))+basket[j+1:]
print(' '.join(map(str, basket)))
