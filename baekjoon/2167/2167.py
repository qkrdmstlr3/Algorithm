"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/2167
"""

import sys


def minus_one(num):
    return num-1


N, M = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
for k in range(int(sys.stdin.readline())):
    i, j, x, y = map(minus_one, map(int, sys.stdin.readline().split()))
    num_sum = 0
    for m in range(i, x+1):
        for n in range(j, y+1):
            num_sum += array[m][n]
    print(num_sum)
