"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/1764
    google 검색 참조 > 집합 사용법
"""

import sys

N, M = map(int, sys.stdin.readline().split())
hear = set()
see = set()
for i in range(N):
    hear.add(sys.stdin.readline().rstrip())
for i in range(M):
    see.add(sys.stdin.readline().rstrip())

hear_and_see = see & hear
print(len(hear_and_see))
for i in sorted(hear_and_see):
    print(i)
