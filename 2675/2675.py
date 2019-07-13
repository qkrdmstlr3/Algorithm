"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2675
"""

import sys

for i in range(int(input())):
    li = list(sys.stdin.readline().split())
    for j in range(len(li[1])):
        print(li[1][j]*int(li[0]), end='')
    print()
