"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10812
"""

import sys


def minus(num):
    return num-1


N, M = map(int, sys.stdin.readline().split())
basket = list(range(1, N+1))
for _ in range(M):
    i, j, k = map(minus, map(int, sys.stdin.readline().split()))
    basket = basket[:i]+basket[k:j+1]+basket[i:k]+basket[j+1:]
print(' '.join(map(str, basket)))
