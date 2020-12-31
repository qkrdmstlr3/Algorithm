"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/10867
"""

import sys

N = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(int(N)):
    if num[i] not in result:
        result.append(num[i])
result.sort()
print(' '.join(map(str, result)))
