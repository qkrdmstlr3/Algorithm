"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1182
    correct percentage : 44.864%
"""

import sys
import itertools

N, S = map(int, sys.stdin.readline().split())
integer = list(map(int, sys.stdin.readline().split()))
sequence_num = 0
for i in range(1, N+1):
    for j in itertools.combinations(integer, i):
        if sum(j) == S:
            sequence_num += 1
print(sequence_num)
