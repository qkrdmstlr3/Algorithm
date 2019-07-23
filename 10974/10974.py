"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/10974
"""

import sys
import itertools

num = list(range(1, int(sys.stdin.readline())+1))
for i in itertools.permutations(num, len(num)):
    print(' '.join(map(str, i)))
