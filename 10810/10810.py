"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10810
    항상 g팀이 이긴다는 것을 고려;;
"""

import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0]*(N+1)

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for m in range(i, j+1):
        basket[m] = k
for m in range(1, len(basket)):
    print(basket[m], end=' ')
