"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/10824
    correct percentage : 41.914%
"""

import sys
from operator import itemgetter

boj = []
for i in range(int(sys.stdin.readline())):
    li = list(sys.stdin.readline().split())
    li[0] = int(li[0])
    boj.append(li)

boj.sort(key=itemgetter(0))
for i in range(len(boj)):
    print(boj[i][0], boj[i][1])
