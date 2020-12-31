"""
    Author : ParkEunsik
    Date   : 2019/07/18
    url    : https://www.acmicpc.net/problem/2309
    correct percentage : 47.474%
"""

import sys
import itertools

ki = [None]*9
for i in range(9):
    ki[i] = int(sys.stdin.readline())

for i in itertools.combinations(ki, 7):
    if sum(i) == 100:
        li = list(i)
        li.sort()
        print("\n".join(map(str, li)))
        break
