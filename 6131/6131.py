"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/6131
"""

import sys
import itertools

N = int(sys.stdin.readline())

count = 0
li = list(range(1, 501))
for i in itertools.combinations(li, 2):
    if i[0]*i[0]+N == i[1]*i[1]:
        count += 1
print(count)
