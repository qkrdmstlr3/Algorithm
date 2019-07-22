"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/10610
"""

import sys
import itertools

N = sys.stdin.readline()
num, result = [], []
for i in range(len(N)-1):
    num.append(N[i])
for i in itertools.permutations(num, len(num)):
    if int(''.join(i)) % 30 == 0:
        result.append(int(''.join(i)))
if not result:
    print(-1)
else:
    result.sort()
    print(result[-1])
