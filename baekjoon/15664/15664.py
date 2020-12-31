"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/15664
"""

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

li = []
for i in itertools.combinations(num, M):
    if ' '.join(map(str, i)) in li:
        continue
    li.append(' '.join(map(str, i)))
for i in range(len(li)):
    print(li[i])
