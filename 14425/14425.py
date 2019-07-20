"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/14425
"""

import sys

N, M = map(int, sys.stdin.readline().split())
word, cnt = [], 0

for i in range(N):
    word.append(sys.stdin.readline())
for i in range(M):
    if sys.stdin.readline() in word:
        cnt += 1
print(cnt)
