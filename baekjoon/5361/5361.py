"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5361
"""

import sys

index = 0
parts = [0, 350.34, 230.90, 190.55, 125.30, 180.90]


def calculate(part):
    global index
    index += 1
    return int(part)*parts[index]


for i in range(int(sys.stdin.readline())):
    num = list(map(calculate, sys.stdin.readline().split()))
    print('${:0.2f}'.format(sum(num)))
    index = 0
