"""
    Author : ParkEunsik
    Date   : 2019/07/15
    url    : https://www.acmicpc.net/problem/11651
"""

import sys
from operator import itemgetter

coor = []
for i in range(int(sys.stdin.readline())):
    coor.append(list(map(int, sys.stdin.readline().split())))

coor.sort(key=itemgetter(1, 0))  # 우선적으로 y정렬하고 그 다음 x 정렬
for i in range(len(coor)):
    print(coor[i][0], coor[i][1])
