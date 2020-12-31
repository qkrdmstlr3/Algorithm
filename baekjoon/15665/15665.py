"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/15665
"""

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))  # 문자로 정렬하면 틀렸다고 나온다;;

for i in itertools.combinations(num, M):
    print(' '.join(map(str, i)))
