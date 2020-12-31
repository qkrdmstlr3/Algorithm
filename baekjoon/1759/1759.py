"""
    Author : ParkEunsik
    Date   : 2019/09/06
    url    : https://www.acmicpc.net/problem/1759
    correct percentage : 44.251%
"""

import sys
import itertools

l, c = map(int, sys.stdin.readline().split())
za = []
mo = []
for i in sorted(list(sys.stdin.readline().split())):
    if i in ['a', 'e', 'i', 'o', 'u']:
        mo.append(i)
    else:
        za.append(i)
result = []
for i in range(len(mo)):
    for j in range(1, len(za)):
        if i+1+j+1 == l:
            for m in itertools.combinations(mo, i+1):
                for n in itertools.combinations(za, j+1):
                    result.append(''.join(sorted(m+n)))
result.sort()
print('\n'.join(result))
