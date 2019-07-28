"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/3040
"""

import sys
import itertools

li = []
for i in range(9):
    li.append(int(sys.stdin.readline()))
for i in itertools.combinations(li, 7):
    if sum(i) == 100:
        print('\n'.join(map(str, i)))
