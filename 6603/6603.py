"""
    Author : ParkEunsik
    Date   : 2019/07/22
    url    : https://www.acmicpc.net/problem/6603
"""

import sys
import itertools

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break
    for i in itertools.combinations(num[1:], 6):
        for j in range(6):
            print(i[j], end=' ')
    print('\n')
